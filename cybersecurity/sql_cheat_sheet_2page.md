# SQL Quick Reference #

### CREATE TABLE — Define a table ###
```sql
CREATE TABLE customers (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255),
    balance DECIMAL(10,2) DEFAULT 0
);
```

### INSERT — Add rows ###
```sql
INSERT INTO customers (id, name, email, balance)
VALUES (1, 'Alice', 'alice@example.com', 100.00);
```

### DROP TABLE — Remove the table ###
```sql
DROP TABLE IF EXISTS customers;
```

### SELECT — Read rows
```sql
SELECT * FROM customers;
SELECT name, email FROM customers WHERE balance > 100;
WHERE balance > 100 AND name = 'Bob';
WHERE balance < 50 OR name = 'Alice';
SELECT * FROM customers ORDER BY balance DESC LIMIT 5;
```

### UPDATE — Change rows
```sql
UPDATE customers SET balance = 500 WHERE id = 1;
UPDATE customers SET balance = balance + 50 WHERE id = 1;
```

### DELETE — Remove rows
```sql
DELETE FROM customers WHERE id = 1;
DELETE FROM customers;  -- Removes ALL rows
```

### Common WHERE conditions
```sql
WHERE id = 1                 -- equal
WHERE id <> 1                -- not equal
WHERE balance >= 100         -- comparison: > < >= <=
WHERE name LIKE 'A%'         -- starts with A
WHERE id IN (1, 2, 3)        -- one of several values
WHERE balance BETWEEN 50 AND 100
WHERE email IS NULL          -- missing value
WHERE balance > 0 AND id < 10 -- combine: AND / OR
```

**Remember:** `UPDATE` or `DELETE` without `WHERE` affects **every row**. Use parameterized queries for user-provided values.
