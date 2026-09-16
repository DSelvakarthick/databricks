# Databricks notebook source
# MAGIC %md
# MAGIC ## Debugging Databricks Notebooks
# MAGIC > Enable Debugger: Settings → Developer → Enable Python notebook interactive debugger 
# MAGIC > 
# MAGIC > Supported Runtime - 13.3 LTS or Higher
# MAGIC > 
# MAGIC > Supported Languages - Only Python at the moment

# COMMAND ----------

# MAGIC %md
# MAGIC #### Demo 1 
# MAGIC Demonstrate 
# MAGIC 1. Breakpoints
# MAGIC 1. Step through code line by line
# MAGIC 1. Variable Explorer
# MAGIC 1. Debug Console

# COMMAND ----------

# Calculate the final price of an item and print that value

item_price = 120.00
tax_rate = 20        # Given as percentage
discount = 10.00

# 1. Calculate the tax to be applied
tax = item_price * (tax_rate / 100)

# 2. Apply tax to the item price
item_price_with_tax = item_price + tax

# 3. Apply the flat discount to the item price
final_price = item_price_with_tax - discount

# Print the final print
print(f"Final Price: {final_price:.2f}")

# COMMAND ----------

# MAGIC %md
# MAGIC #### Demo 2 
# MAGIC Demonstrate Step In and Step Out

# COMMAND ----------

def calculate_final_price(item_price, tax_rate, discount):
    # 1. Calculate the tax to be applied
    tax = item_price * (tax_rate / 100)
    
    # 2. Apply tax to the item price
    item_price_with_tax = item_price + tax

    # 3. Apply the flat discount to the item price
    final_price = item_price_with_tax - discount
    return final_price

# COMMAND ----------

# Main program
item_price = 120.00
tax_rate = 20        # Given as percentage
discount = 10.00

final_price = calculate_final_price(item_price, tax_rate, discount)  

print(f"Final Price: {final_price:.2f}")
