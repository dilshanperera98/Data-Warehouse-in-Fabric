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