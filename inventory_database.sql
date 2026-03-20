-- Active: 1772520994257@@127.0.0.1@3306@credit_risk_db
SELECT * FROM sales_data LIMIT 5;
DESCRIBE sales_data;

-- Check total records
SELECT COUNT(*) AS total_records
FROM sales_data;

-- ===============================================
-- Inventory Optimization Project SQL Queries
-- ===============================================

-- 1. Select Database
USE inventory_optimization;

-- ===============================================
-- 2. View All Data
-- ===============================================
SELECT *
FROM sales_data;


-- ===============================================
-- 3. Total Sales in Dataset
-- ===============================================
SELECT 
    SUM(sales) AS total_sales
FROM sales_data;


-- ===============================================
-- 4. Sales by Category
-- ===============================================
SELECT 
    category,
    SUM(sales) AS total_sales
FROM sales_data
GROUP BY category
ORDER BY total_sales DESC;


-- ===============================================
-- 5. Sales by Sub-Category
-- ===============================================
SELECT 
    `Sub-Category`,
    SUM(sales) AS total_sales
FROM sales_data
GROUP BY `Sub-Category`
ORDER BY total_sales DESC;


-- ===============================================
-- 6. Top 10 Best Selling Products
-- ===============================================
SELECT 
    `Product Name`,
    SUM(Sales) AS total_sales
FROM sales_data
GROUP BY `Product Name`
ORDER BY total_sales DESC
LIMIT 10;


-- ===============================================
-- 7. Region-Wise Sales Analysis
-- ===============================================
SELECT 
    region,
    SUM(sales) AS total_sales
FROM sales_data
GROUP BY region
ORDER BY total_sales DESC;


-- ===============================================
-- 8. State-Wise Sales Analysis
-- ===============================================
SELECT 
    state,
    SUM(sales) AS total_sales
FROM sales_data
GROUP BY state
ORDER BY total_sales DESC;


-- ===============================================
-- 9. Top 10 Cities by Sales
-- ===============================================
SELECT 
    city,
    SUM(sales) AS total_sales
FROM sales_data
GROUP BY city
ORDER BY total_sales DESC
LIMIT 10;


-- ===============================================
-- 10. Monthly Sales Trend
-- ===============================================
SELECT 
    MONTH(`Order Date`) AS month,
    SUM(Sales) AS monthly_sales
FROM sales_data
GROUP BY MONTH(`Order Date`)
ORDER BY month;


-- ===============================================
-- 11. Sales by Customer Segment
-- ===============================================
SELECT 
    segment,
    SUM(sales) AS total_sales
FROM sales_data
GROUP BY segment
ORDER BY total_sales DESC;


-- ===============================================
-- 12. Average Shipping Time
-- ===============================================
SELECT 
    AVG(DATEDIFF(`Ship Date`, `Order Date`)) AS avg_shipping_days
FROM sales_data;


-- ===============================================
-- 13. Orders by Shipping Mode
-- ===============================================
SELECT 
    `Ship Mode`,
    COUNT(*) AS total_orders
FROM sales_data
GROUP BY `Ship Mode`
ORDER BY total_orders DESC;


-- ===============================================
-- 14. Average Sales per Product
-- ===============================================
SELECT 
    `Product Name`,
    AVG(Sales) AS average_sales
FROM sales_data
GROUP BY `Product Name`
ORDER BY average_sales DESC;


-- ===============================================
-- 15. Category Sales Contribution (%)
-- ===============================================
SELECT 
    category,
    SUM(sales) AS total_sales,
    ROUND(
        SUM(sales) * 100 /
        (SELECT SUM(sales) FROM sales_data),
        2
    ) AS sales_percentage
FROM sales_data
GROUP BY category
ORDER BY total_sales DESC;


-- ===============================================
-- 16. High Demand Products
-- ===============================================
SELECT 
    `Product Name`,
    SUM(Sales) AS total_sales
FROM sales_data
GROUP BY `Product Name`
HAVING SUM(Sales) > 5000
ORDER BY total_sales DESC;