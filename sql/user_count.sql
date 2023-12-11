-- Count the total users in the User table
SELECT COUNT(DISTINCT email_address) as user_count
FROM User;

-- Select the full User table
-- SELECT *
-- FROM User;


--  count the distinct number of email domains in the User table and group by email address, order by count desc. This is a sqlite3 DB
-- SELECT substr(email_address, instr(email_address, '@') + 1) as domain, COUNT(DISTINCT email_address) as email_count
-- FROM User
-- GROUP BY domain
-- ORDER BY email_count DESC;


-- show the schema of the User table for a sqlite3 database
--.schema User


-- which customer bought the most products?
-- SELECT U.email_address, COUNT(O.product_id) as product_purchases
-- FROM User U
-- JOIN Orders O ON U.customer_id = O.customer_id
-- GROUP BY U.email_address
-- ORDER BY product_purchases DESC;
