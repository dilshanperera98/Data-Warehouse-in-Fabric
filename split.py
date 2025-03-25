import pandas as pd
import os

# Load Excel file
df = pd.read_excel("/Users/dilshanperera/Desktop/Cargills/Codes/dataset/sales_data_sample.xlsx")

# Ensure 'CUSTOMERNAME' exists
if 'CUSTOMERNAME' not in df.columns:
    raise KeyError("CUSTOMERNAME column not found in the dataset. Check column names.")

# Extract Customer Dimension (Unique Customers)
dim_customer = df[['CUSTOMERNAME', 'PHONE', 'ADDRESSLINE1', 'ADDRESSLINE2',
                   'CITY', 'STATE', 'POSTALCODE', 'COUNTRY', 'TERRITORY',
                   'CONTACTLASTNAME', 'CONTACTFIRSTNAME']].drop_duplicates()
 
# Assign Customer ID
dim_customer.insert(0, 'CUSTOMER_ID', range(1, len(dim_customer) + 1))
dim_customer['TABLE_NAME'] = 'Dim_Customer'

# Extract Product Dimension (Unique Products)
dim_product = df[['PRODUCTCODE', 'PRODUCTLINE', 'MSRP']].drop_duplicates()
dim_product['TABLE_NAME'] = 'Dim_Product'

# Extract Time Dimension
dim_time = df[['ORDERDATE', 'YEAR_ID', 'MONTH_ID', 'QTR_ID']].drop_duplicates()
dim_time['TABLE_NAME'] = 'Dim_Time'

# Extract Status Dimension
dim_status = df[['STATUS']].drop_duplicates().reset_index(drop=True)
dim_status.insert(0, 'STATUS_ID', range(1, len(dim_status) + 1))
dim_status['TABLE_NAME'] = 'Dim_Status'

# Extract Fact Table (Sales Transactions)
fact_sales = df[['CUSTOMERNAME', 'ORDERNUMBER', 'PRODUCTCODE', 'ORDERDATE',
                 'QUANTITYORDERED', 'PRICEEACH', 'SALES', 'ORDERLINENUMBER', 
                 'STATUS', 'DEALSIZE']]
fact_sales['TABLE_NAME'] = 'Fact_Sales'

# Merge Fact Table with Dim Tables
fact_sales = fact_sales.merge(dim_customer[['CUSTOMERNAME', 'CUSTOMER_ID']], on='CUSTOMERNAME', how='left')
fact_sales = fact_sales.merge(dim_status[['STATUS', 'STATUS_ID']], on='STATUS', how='left')

# Combine all DataFrames
combined_df = pd.concat([
    dim_customer, 
    dim_product, 
    dim_time, 
    dim_status, 
    fact_sales
], ignore_index=True)

# Define Output Directory and Filename
output_dir = "/Users/dilshanperera/Desktop/Cargills/Codes/outputs"
output_filename = "sales_data_consolidated.csv"

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Full path for the CSV file
output_path = os.path.join(output_dir, output_filename)

# Save the combined DataFrame to a single CSV file
combined_df.to_csv(output_path, index=False)

print(f"CSV file saved successfully at: {output_path}")

# Verify the contents of the CSV
df_verify = pd.read_csv(output_path)
print("\nConsolidated CSV Details:")
print(f"Total rows: {len(df_verify)}")
print(f"Columns: {', '.join(df_verify.columns)}")

# Count rows per table
print("\nRows per Table:")
table_counts = df_verify['TABLE_NAME'].value_counts()
print(table_counts)