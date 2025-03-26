#!/usr/bin/env python
# coding: utf-8

# ## CheckEmptyValues
# 
# New notebook

# Check the how many empty values are there in column wise in sales table

# In[2]:


from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, when

# Initialize Spark Session (with additional configurations if necessary)
spark = SparkSession.builder \
    .appName("EmptyValuesCount") \
    .config("spark.sql.shuffle.partitions", "4") \
    .getOrCreate()

# Define file path
file_path = "Files/fact_sales.csv"

# Load CSV file
df = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load(file_path)

# Function to count empty/null values
def count_empty_values(dataframe):
    # Count null values for each column
    null_counts = dataframe.select([
        count(when(col(c).isNull() | (col(c) == ''), c)).alias(c + '_null_count') 
        for c in dataframe.columns
    ])
    
    # Count total rows for percentage calculation
    total_rows = dataframe.count()
    
    # Display results
    print(f"Total number of rows: {total_rows}")
    print("\nEmpty/Null Values Count and Percentage:")
    null_counts.show(truncate=False)
    
    # Optional: Print percentage of null values
    print("\nPercentage of Null Values:")
    for column in dataframe.columns:
        null_count = null_counts.select(column + '_null_count').collect()[0][0]
        percentage = (null_count / total_rows) * 100
        print(f"{column}: {percentage:.2f}%")

# Call the function
count_empty_values(df)

# Optional: Close Spark session
spark.stop()


# 
