SELECT
t.amount,
c.name,
a.account_name
FROM Transactions as t
LEFT JOIN Categories c ON t.categoryId = c.id
LEFT JOIN Accounts a ON t.accountId = a.id
WHERE t.amount >= 1000