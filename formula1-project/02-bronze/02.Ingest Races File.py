# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "5"
# ///
# MAGIC %md
# MAGIC # Ingest races.csv file
# MAGIC 1. Read the file using spark dataframe reader API
# MAGIC 1. Add Metadata Columns 
# MAGIC     - Source File
# MAGIC     - Ingestion Timestamp
# MAGIC 1. Write to bronze delta table    

# COMMAND ----------

# MAGIC %run ../00-common/01.environment-config

# COMMAND ----------

# MAGIC %run ../00-common/02.bronze-helpers

# COMMAND ----------

if "landing_folder_path" not in globals():
    from pathlib import Path
    from runpy import run_path

    common_folder = Path(__file__).resolve().parents[1] / "00-common"
    globals().update(run_path(str(common_folder / "01.environment-config.py")))
    globals().update(run_path(str(common_folder / "02.bronze-helpers.py")))

if "spark" not in globals():
    import os
    from dotenv import load_dotenv
    from databricks.connect import DatabricksSession

    load_dotenv()
    session_builder = DatabricksSession.builder
    if (
        os.getenv("DATABRICKS_SERVERLESS", "").lower() == "true"
        or not os.getenv("DATABRICKS_CLUSTER_ID")
    ):
        session_builder = session_builder.serverless()
    spark = session_builder.getOrCreate()

if "display" not in globals():
    def display(dataframe):
        dataframe.show(truncate=False)

source_file = f"{landing_folder_path}/races.csv"
table_name = f"{catalog_name}.{bronze_schema}.races"

# COMMAND ----------

# MAGIC %md
# MAGIC #### Step 1 - Read the CSV file using the dataframe reader API

# COMMAND ----------

from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DateType

races_schema = StructType([
    StructField('season',   IntegerType()),
    StructField("round",    IntegerType()),
    StructField("url",      StringType()),
    StructField("raceName", StringType()),
    StructField("date",     DateType()),
    StructField("circuitId", StringType())
])

# COMMAND ----------

races_df = (
    spark.read
         .format('csv')
         .option('header', 'true')
#         .option('inferSchema', 'true')
         .option('mode', 'FAILFAST')
         .schema(races_schema)
         .load(source_file)
)

# COMMAND ----------

display(races_df)

# COMMAND ----------

# MAGIC %md
# MAGIC #### Step 2 - Add Metadata Columns
# MAGIC - Source File
# MAGIC - Ingestion Timestamp

# COMMAND ----------

races_final_df = add_ingestion_metadata(races_df)

# COMMAND ----------

display(races_final_df)

# COMMAND ----------

# MAGIC %md
# MAGIC #### Step 3 - Write to bronze delta table

# COMMAND ----------

(
    races_final_df
        .write
        .format('delta')
        .mode('overwrite')
        .saveAsTable(table_name)
)

# COMMAND ----------

display(spark.table(table_name))