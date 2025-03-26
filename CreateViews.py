#!/usr/bin/env python
# coding: utf-8

# ## CreateViews
# 
# New notebook

# In[4]:


-- Top Selling Products View
CREATE VIEW vw_TopSellingProducts AS
SELECT 
    s.PRODUCTCODE,
    p.PRODUCTLINE,
    SUM(CAST(s.QUANTITYORDERED AS INT)) AS TotalQuantity,
    SUM(CAST(s.SALES AS DECIMAL(18,2))) AS TotalRevenue,
    RANK() OVER (ORDER BY SUM(CAST(s.SALES AS DECIMAL(18,2))) DESC) AS RevenueRank,
    RANK() OVER (ORDER BY SUM(CAST(s.QUANTITYORDERED AS INT)) DESC) AS QuantityRank
FROM fact_sales s
JOIN dim_product p ON s.PRODUCTCODE = p.PRODUCTCODE
GROUP BY s.PRODUCTCODE, p.PRODUCTLINE;


# In[7]:


-- Monthly Revenue Trend View
CREATE VIEW vw_MonthlyRevenueTrend AS
SELECT 
    t.YEAR_ID,
    t.MONTH_ID,
    SUM(CAST(s.SALES AS DECIMAL(18,2))) AS TotalRevenue,  -- Ensure SALES is numeric
    COUNT(DISTINCT s.ORDERNUMBER) AS OrderCount
FROM fact_sales s
JOIN dim_time t ON s.ORDERDATE = t.ORDERDATE
GROUP BY t.YEAR_ID, t.MONTH_ID;



# In[16]:


-- Order Status Distribution View
CREATE VIEW vw_OrderStatusDistribution AS
SELECT 
    st.STATUS,
    COUNT(DISTINCT s.ORDERNUMBER) AS OrderCount,
    SUM(CAST(s.SALES AS DECIMAL(18, 2))) AS TotalRevenue
FROM fact_sales s
JOIN dim_status st ON s.STATUS_ID = st.STATUS_ID
GROUP BY st.STATUS;



# In[20]:


-- Customer Deal Size Distribution View
CREATE VIEW vw_CustomerDealSizeDistribution AS
SELECT 
    DEALSIZE,
    COUNT(DISTINCT ORDERNUMBER) AS OrderCount,
    COUNT(DISTINCT CUSTOMER_ID) AS CustomerCount,
    SUM(CAST(SALES AS DECIMAL(18, 2))) AS TotalRevenue,
    AVG(CAST(SALES AS DECIMAL(18, 2))) AS AvgDealAmount
FROM fact_sales
GROUP BY DEALSIZE;


# In[27]:


-- Get the Year Wise Sales Data
CREATE PROCEDURE sp_GetYearlySalesData
AS
BEGIN
    SELECT 
        t.YEAR_ID,
        SUM(CAST(s.SALES AS DECIMAL(18, 2))) AS TotalRevenue,  -- Casting SALES to numeric
        COUNT(DISTINCT s.ORDERNUMBER) AS OrderCount,
        SUM(CAST(s.QUANTITYORDERED AS INT)) AS TotalQuantity  -- Casting QUANTITYORDERED to numeric (INT)
    FROM fact_sales s
    JOIN dim_time t ON s.ORDERDATE = t.ORDERDATE
    GROUP BY t.YEAR_ID
    ORDER BY t.YEAR_ID;
END;

