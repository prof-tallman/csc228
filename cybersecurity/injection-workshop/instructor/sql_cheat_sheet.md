## SQL Quick Reference ##

### SELECT — Read rows ###
```sql
  SELECT * FROM customers;
  SELECT name, email FROM customers WHERE (balance > 100 AND name = 'Bob');
  SELECT name, email FROM customers WHERE (balance < 50 OR name = 'Alice');
  SELECT * FROM customers ORDER BY balance DESC LIMIT 5;
```

### DELETE — Remove rows ###
```sql
  DELETE FROM customers WHERE id = 1;
  DELETE FROM customers;       -- Removes ALL rows
```

### UPDATE — Change rows ###
```sql
  UPDATE customers SET balance = 500 WHERE id = 1;
  UPDATE customers SET balance = balance + 50 WHERE id <> 1;
```

### Common WHERE conditions ###
```sql
  WHERE id = 1                       -- equal
  WHERE id <> 1                      -- not equal
  WHERE balance >= 100               -- comparison: > < >= <=
  WHERE name LIKE 'A%'               -- starts with A
  WHERE id IN (1, 2, 3)              -- one of several values
  WHERE email IS NULL                -- missing value
  WHERE balance > 0 AND id < 10      -- can combine AND / OR
  WHERE balance < 50 OR late > 3     --   with parenthesis 
```

**Remember:** `UPDATE` or `DELETE` without `WHERE` affects **every row**.
