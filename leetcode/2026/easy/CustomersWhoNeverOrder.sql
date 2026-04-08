SELECT
c.name
FROM Customers as c
LEFT JOIN Orders o ON p.id = o.customerId
WHERE c.id is NULL;