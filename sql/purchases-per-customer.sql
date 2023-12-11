SELECT U.email_address, COUNT(O.product_id) as product_purchases
FROM User U
JOIN Orders O ON U.customer_id = O.customer_id
GROUP BY U.email_address
ORDER BY product_purchases DESC;

