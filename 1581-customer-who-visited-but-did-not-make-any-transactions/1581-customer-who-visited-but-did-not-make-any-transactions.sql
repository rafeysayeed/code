/* Write your T-SQL query statement below */
SELECT customer_id, COUNT(customer_id) AS count_no_trans
FROM Visits V 
FULL OUTER JOIN Transactions T 
ON V.visit_id = T.visit_id 
WHERE V.visit_id IS NULL 
OR 
T.visit_id IS NULL
GROUP BY customer_id
ORDER BY count_no_trans