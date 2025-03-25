End-to-End Data Warehouse Implementation Guide for Sales Data in Microsoft Fabric
1. Introduction to Microsoft Fabric
Microsoft Fabric is an all-in-one analytics solution that provides a comprehensive platform for data integration, warehousing, and business intelligence. It combines various Microsoft services into a unified environment.
2. Prerequisites

Microsoft 365 Account
Power BI Pro or Premium License
Basic understanding of data warehousing concepts

3. Project Setup in Microsoft Fabric
3.1 Creating a Fabric Workspace

Open Microsoft Power BI
Click on "Workspaces" in the left navigation pane
Select "Create a workspace"
Name your workspace (e.g., "Sales Data Warehouse Project")
Choose a licensing mode (Power BI Premium or shared)

3.2 Data Warehouse Architecture Design
Our data warehouse will follow a star schema with the following components:

Dimension Tables:

dim_customer
dim_time
dim_product
dim_status


Fact Table:

fact_sales



3.3 Data Ingestion and Transformation
Step 1: Uploading Source Data

In your Fabric Workspace, select "OneLake"
Create a new Lakehouse (e.g., "SalesDataLakehouse")
Upload your Excel file to the Lakehouse

Step 2: Data Transformation with Dataflow Gen2

Create a new Dataflow Gen2 in your workspace
Connect to your uploaded Excel file
Perform initial data transformations:

Clean column names
Remove duplicates
Handle null values
Create proper data types



