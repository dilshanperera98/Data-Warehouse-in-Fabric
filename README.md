# Data Warehouse Solution for Sales Data

## Project Overview

This project aims to design a data warehouse solution to store, transform, and organize raw sales data into a meaningful and efficient reporting structure. The goal is to use Microsoft Fabric to create a comprehensive data warehouse system, demonstrating the integration of data sources and providing insightful reports through Power BI. The solution will also leverage Python, SQL, and PySpark for data transformation and automation.

## Objectives

- **Data Warehouse Design**: Develop a data warehouse architecture that efficiently organizes and integrates raw sales data, enabling seamless reporting and analysis.
- **Data Transformation**: Use Python, SQL, and/or PySpark scripts to transform and manipulate the raw data, creating the necessary tables for storage and reporting.
- **Power BI Dashboard**: Create a Power BI dashboard that presents insightful and visually appealing sales reports derived from the transformed data.

## Components

### 1. Data Warehouse Design
The data warehouse design outlines the architecture, data modeling, and structure required to store and manage the sales data effectively. Key elements include:
- **Star Schema**: Use of fact and dimension tables for optimal data organization.
- **Fact Tables**: Storing aggregated sales data such as total sales, quantities sold, and transaction details.
- **Dimension Tables**: Storing descriptive data such as products, customers, time, and locations.
- **ETL Process**: Extract, transform, and load (ETL) processes that will clean and structure the data for analysis.
  
The design will be based on a **Star Schema** with relevant relationships between facts and dimensions, ensuring scalability and easy reporting.

### 2. Data Transformation Scripts
The project will include scripts developed using **Python**, **SQL**, and **PySpark** to transform the raw sales data into structured tables that can be stored in the data warehouse. These scripts will:
- **Extract** raw data from CSV or database sources.
- **Transform** the data by cleaning, aggregating, and structuring it into appropriate formats.
- **Load** the data into fact and dimension tables for reporting.

Example scripts will be included in this project to demonstrate:
- Data extraction from CSV or database.
- SQL-based data transformations.
- Data aggregation and cleansing using Python and PySpark.

### 3. Power BI Dashboard
A simple **Power BI dashboard** will be created to present the transformed sales data in a meaningful way. The dashboard will include:
- **Key Metrics**: Total sales, sales by product/category, customer demographics, etc.
- **Visualizations**: Charts, graphs, and tables to display trends, comparisons, and insights from the data.
- **Interactivity**: Filters and slicers for users to explore data based on different dimensions (e.g., time, product, region).

## Tools and Technologies

- **Microsoft Fabric**: To build the data warehouse solution and automate the process.
- **Python**: For data manipulation and automation.
- **SQL**: For database interactions and querying.
- **PySpark**: For big data processing and transformation.
- **Power BI**: For creating interactive dashboards and reports.


## Project Structure

This project demonstrates the steps taken to process and normalize data, build a data lakehouse, transfer the data to a data warehouse, and create real-time reporting via Power BI.

## 1. Initial Data Exploration and Normalization
- **Step 1.1**: Thoroughly reviewed the original Excel dataset to understand the data structure and its contents.
- **Step 1.2**: Identified a single table containing all the data in the Excel sheet.
- **Step 1.3**: Performed data normalization by transforming the data into a star schema using a custom Python script:
  - Breaking the data into fact and dimension tables.
  - Ensuring data consistency and establishing relationships between tables.
- **Step 1.4**: Exported the normalized tables as separate CSV files.
- **Step 1.5**: Conducted an initial data quality check:
  - Verified the correctness of the normalized data.
  - Checked for missing or null values.
  - Ensured data consistency and accuracy.
  - Performed basic data validation techniques to identify and resolve any issues.
 
<img width="1440" alt="01" src="https://github.com/user-attachments/assets/fd7f9d21-abaf-4f14-9a44-fe48eee14823" />



## 2. Creating the Data Lakehouse
- **Step 2.1**: Designed and created a Data Lakehouse named `Sales_Lakehouse` to store the normalized data.
- **Step 2.2**: Utilized PySpark in a Jupyter Notebook to interact with the data and perform necessary checks.
- **Step 2.3**: Checked for missing values (null values) in each column and identified the percentage of nulls in the dataset.
- **Step 2.4**: Identified and handled any duplicated data in the dataset, ensuring data integrity.
- **Step 2.5**: Stored the cleaned and transformed data in the Data Lakehouse, which served as the source for further analysis.

## 3. Building the Data Warehouse
- **Step 3.1**: Designed and implemented a Data Warehouse based on the project requirements.
- **Step 3.2**: Structured the data warehouse for optimized storage and easy querying, enabling large-scale data analysis.

## 4. Data Transfer Pipeline to Data Warehouse
- **Step 4.1**: Created a data transfer pipeline to move the data from the Data Lakehouse to the Data Warehouse. The pipeline ensured that data was ingested, transformed, and loaded (ETL process) into the warehouse seamlessly.
- **Step 4.2**: Automated the transfer process to ensure that the data is always up-to-date and available for reporting and analysis.

## 5. SQL Views and Stored Procedures
- **Step 5.1**: Created SQL views in the Data Warehouse to facilitate easy querying and reporting of the data.
- **Step 5.2**: Developed stored procedures to encapsulate complex business logic and automate routine tasks.
- **Step 5.3**: Linked the SQL views and stored procedures with Power BI for real-time reporting and visualization.

## 6. Final Steps: Linking Power BI
- **Step 6.1**: Established a connection between Power BI and the SQL views in the Data Warehouse.
- **Step 6.2**: Used Power BI to create dynamic dashboards and visualizations for business reporting.
- **Step 6.3**: Ensured that the Power BI dashboards were connected to the latest data in the Data Warehouse, providing real-time insights for decision-makers.

## Technologies Used
- Python
- PySpark
- SQL (Data Warehouse, Views, Stored Procedures)
- Power BI
- Data Lakehouse architecture

This project provides an end-to-end pipeline for data processing, storage, and real-time reporting, enabling efficient decision-making and business analysis.

