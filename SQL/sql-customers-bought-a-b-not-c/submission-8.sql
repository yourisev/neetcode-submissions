SELECT 
    DISTINCT c.customer_id, 
    c.customer_name
FROM customers c
JOIN orders a ON c.customer_id = a.customer_id AND a.product_name = 'A'
JOIN orders b ON c.customer_id = b.customer_id AND b.product_name = 'B'
LEFT JOIN orders pf ON c.customer_id = pf.customer_id AND pf.product_name = 'C'
WHERE pf.product_name IS NULL
ORDER BY c.customer_name;