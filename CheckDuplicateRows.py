#!/usr/bin/env python
# coding: utf-8

# ## CheckDuplicateRows
# 
# New notebook

# Check for Duplicate Rows

# In[1]:


from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("DuplicateRowsCount") \
    .config("spark.sql.shuffle.partitions", "4") \
    .getOrCreate()

# Define file paths
file_paths = {
    "Fact_Sales": "Files/fact_sales.csv",
    "Dim_Customer": "Files/dim_customer.csv",
    "Dim_Product": "Files/dim_product.csv"
}

# Function to count duplicate rows
def count_duplicates(dataframe, table_name):
    duplicate_rows = dataframe.groupBy(dataframe.columns).count().filter(col("count") > 1)
    duplicate_count = duplicate_rows.count()

    print(f"\nTable: {table_name}")
    print(f"Total Duplicate Rows: {duplicate_count}")

# Load and process each dataset
for table_name, path in file_paths.items():
    df = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load(path)
    count_duplicates(df, table_name)

# Close Spark session
spark.stop()

