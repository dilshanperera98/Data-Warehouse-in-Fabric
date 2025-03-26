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

The project directory structure is as follows:

