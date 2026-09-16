-- Databricks notebook source
-- MAGIC %md
-- MAGIC # Understanding Delta Lake Transaction Log
-- MAGIC Understand the cloud storage directory structure for a delta table 

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #### 1. Create Catalog and Schema for the Demo
-- MAGIC **Catalog:** demo  
-- MAGIC **Schema:** delta_lake

-- COMMAND ----------

CREATE CATALOG IF NOT EXISTS demo
MANAGED LOCATION 'abfss://demo@databrickscourseextdl1.dfs.core.windows.net/'

-- COMMAND ----------

CREATE SCHEMA IF NOT EXISTS demo.delta_lake
MANAGED LOCATION 'abfss://demo@databrickscourseextdl1.dfs.core.windows.net/delta_lake'

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #### 1. Create a Delta Lake Table

-- COMMAND ----------

CREATE TABLE IF NOT EXISTS demo.delta_lake.companies
(
  company_name STRING,
  founded_date DATE,
  country      STRING
)
USING DELTA;

-- COMMAND ----------

DESC EXTENDED demo.delta_lake.companies;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #### 2. Insert Some Data

-- COMMAND ----------

INSERT INTO demo.delta_lake.companies
VALUES ('Apple', '1976-04-01', 'USA')

-- COMMAND ----------

SELECT * FROM demo.delta_lake.companies;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #### 3. Insert More Data

-- COMMAND ----------

INSERT INTO demo.delta_lake.companies
VALUES
  ('Microsoft', '1975-04-04', 'USA'),
  ('Google',  '1998-09-04', 'USA'),
  ('Amazon',  '1994-07-05', 'USA');

-- COMMAND ----------

SELECT * FROM demo.delta_lake.companies;