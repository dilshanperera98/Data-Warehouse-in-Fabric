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

# Extract Product Dimension (Unique Products)
dim_product = df[['PRODUCTCODE', 'PRODUCTLINE', 'MSRP']].drop_duplicates()

# Extract Time Dimension
dim_time = df[['ORDERDATE', 'YEAR_ID', 'MONTH_ID', 'QTR_ID']].drop_duplicates()

# Extract Status Dimension
dim_status = df[['STATUS']].drop_duplicates().reset_index(drop=True)
dim_status.insert(0, 'STATUS_ID', range(1, len(dim_status) + 1))

# Extract Fact Table (Sales Transactions)
fact_sales = df[['CUSTOMERNAME', 'ORDERNUMBER', 'PRODUCTCODE', 'ORDERDATE',
                 'QUANTITYORDERED', 'PRICEEACH', 'SALES', 'ORDERLINENUMBER', 
                 'STATUS', 'DEALSIZE']]

# Merge Fact Table with Dim Tables
fact_sales = fact_sales.merge(dim_customer[['CUSTOMERNAME', 'CUSTOMER_ID']], on='CUSTOMERNAME', how='left')
fact_sales = fact_sales.merge(dim_status[['STATUS', 'STATUS_ID']], on='STATUS', how='left')

# Define Output Directory
output_dir = "/Users/dilshanperera/Desktop/Cargills/Codes/outputs"

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Excel Filename
excel_filename = "sales_data_consolidated.xlsx"
excel_path = os.path.join(output_dir, excel_filename)

# CSV Filename
csv_filename = "sales_data_consolidated.csv"
csv_path = os.path.join(output_dir, csv_filename)

# Create Excel file with multiple sheets
with pd.ExcelWriter(excel_path, engine='xlsxwriter') as writer:
    fact_sales.to_excel(writer, sheet_name='Fact_Sales', index=False)
    dim_customer.to_excel(writer, sheet_name='Dim_Customer', index=False)
    dim_product.to_excel(writer, sheet_name='Dim_Product', index=False)
    dim_time.to_excel(writer, sheet_name='Dim_Time', index=False)
    dim_status.to_excel(writer, sheet_name='Dim_Status', index=False)

print(f"Excel file saved successfully at: {excel_path}")

# Create combined CSV
# Add a column to identify the source of each row
fact_sales['TABLE_NAME'] = 'Fact_Sales'
dim_customer['TABLE_NAME'] = 'Dim_Customer'
dim_product['TABLE_NAME'] = 'Dim_Product'
dim_time['TABLE_NAME'] = 'Dim_Time'
dim_status['TABLE_NAME'] = 'Dim_Status'

# Combine all DataFrames
combined_df = pd.concat([
    fact_sales, 
    dim_customer, 
    dim_product, 
    dim_time, 
    dim_status
], ignore_index=True)

# Save combined DataFrame to CSV
combined_df.to_csv(csv_path, index=False)
print(f"CSV file saved successfully at: {csv_path}")

# Verify the contents of the Excel file
print("\nExcel Sheet Details:")
excel_file = pd.ExcelFile(excel_path)
for sheet_name in excel_file.sheet_names:
    df = pd.read_excel(excel_path, sheet_name=sheet_name)
    print(f"{sheet_name}: {len(df)} rows, {len(df.columns)} columns")

# Verify the contents of the CSV
df_verify = pd.read_csv(csv_path)
print("\nConsolidated CSV Details:")
print(f"Total rows: {len(df_verify)}")
print(f"Columns: {', '.join(df_verify.columns)}")

# Count rows per table
print("\nRows per Table:")
table_counts = df_verify['TABLE_NAME'].value_counts()
print(table_counts)