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
fact_sales = fact_sales.merge(dim_customer, on='CUSTOMERNAME', how='left')
fact_sales = fact_sales.merge(dim_status, on='STATUS', how='left')

# Define Output Directory
output_dir = "/Users/dilshanperera/Desktop/Cargills/Codes/outputs"

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Define Output File Path
output_file = os.path.join(output_dir, "sales_data_output.csv")

# Create a list to store all DataFrames with separators
csv_sections = []

# Add each DataFrame with a separator
csv_sections.append(pd.DataFrame({'Sheet': ['dim_customer']}))
csv_sections.append(dim_customer)
csv_sections.append(pd.DataFrame({'Sheet': ['dim_product']}))
csv_sections.append(dim_product)
csv_sections.append(pd.DataFrame({'Sheet': ['dim_time']}))
csv_sections.append(dim_time)
csv_sections.append(pd.DataFrame({'Sheet': ['dim_status']}))
csv_sections.append(dim_status)
csv_sections.append(pd.DataFrame({'Sheet': ['fact_sales']}))
csv_sections.append(fact_sales)

# Combine all sections
combined_df = pd.concat(csv_sections, ignore_index=True)

# Save to CSV
combined_df.to_csv(output_file, index=False)

print(f"CSV file saved successfully at: {output_file}")

# Print details about the output
print("\nOutput Details:")
print(f"Total rows: {len(combined_df)}")
print("\nRows per sheet:")
print(f"dim_customer: {len(dim_customer)} rows")
print(f"dim_product: {len(dim_product)} rows")
print(f"dim_time: {len(dim_time)} rows")
print(f"dim_status: {len(dim_status)} rows")
print(f"fact_sales: {len(fact_sales)} rows")