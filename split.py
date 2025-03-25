import pandas as pd

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
fact_sales = fact_sales.merge(dim_customer, on='CUSTOMERNAME', how='left')
fact_sales = fact_sales.merge(dim_status, on='STATUS', how='left')

# Define Output File Path
output_file = "/Users/dilshanperera/Desktop/Cargills/Codes/outputs/sales_data_output.xlsx"

# Save DataFrames to an Excel file with multiple sheets
with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
    dim_customer.to_excel(writer, sheet_name="dim_customer", index=False)
    dim_product.to_excel(writer, sheet_name="dim_product", index=False)
    dim_time.to_excel(writer, sheet_name="dim_time", index=False)
    dim_status.to_excel(writer, sheet_name="dim_status", index=False)
    fact_sales.to_excel(writer, sheet_name="fact_sales", index=False)

print(f"Excel file saved successfully at: {output_file}")
