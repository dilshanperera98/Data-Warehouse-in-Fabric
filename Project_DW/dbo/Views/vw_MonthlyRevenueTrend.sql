-- Auto Generated (Do not modify) 72F41106ABDF8B1960CA73B571930202E40905129792FE4C01B9A66DF2A8E20F
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