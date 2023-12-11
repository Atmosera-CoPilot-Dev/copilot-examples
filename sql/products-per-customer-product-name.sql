-- Find the number of purchases of each product by each customer.
-- SELECT U.email_address, P.product_name, COUNT(O.product_id) as product_purchases
-- FROM User U
-- JOIN Orders O ON U.customer_id = O.customer_id
-- JOIN Products P ON O.product_id = P.product_id
-- GROUP BY U.email_address, P.product_name
-- ORDER BY product_purchases DESC;


-- write a query that tells me the top selling product
SELECT P.product_name, COUNT(O.product_id) as product_sales
FROM Orders O
JOIN Products P ON O.product_id = P.product_id
GROUP BY P.product_name
ORDER BY product_sales DESC