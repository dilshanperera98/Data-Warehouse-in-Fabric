-- Auto Generated (Do not modify) 80032C6EEA5D26648994B5AC9E03090D151ABE20A3A0983C04F6B5CEC9D7622A
-- Order Status Distribution View
CREATE VIEW vw_OrderStatusDistribution AS
SELECT 
    st.STATUS,
    COUNT(DISTINCT s.ORDERNUMBER) AS OrderCount,
    SUM(CAST(s.SALES AS DECIMAL(18, 2))) AS TotalRevenue
FROM fact_sales s
JOIN dim_status st ON s.STATUS_ID = st.STATUS_ID
GROUP BY st.STATUS;