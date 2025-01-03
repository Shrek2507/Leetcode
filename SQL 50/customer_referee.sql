-- Find Customer Referee
/*
Find the names of the customer that are not referred by the customer with id = 2. Return the result table in any order.
The result format is in the following example.
*/


-- Approach 1
SELECT name 
FROM Customer 
WHERE referee_id !=2 
OR referee_id IS NULL;

#Approach 2
SELECT name
FROM Customer
WHERE id NOT IN (SELECT id FROM Customer WHERE referee_id = 2);

#Approach 3
SELECT name
FROM Customer
WHERE CASE 
        WHEN referee_id != 2 THEN 1
        WHEN referee_id IS NULL THEN 1
        ELSE 0
      END = 1;

# My SQL Query
/* Write your T-SQL query statement below */
select name from Customer where referee_id not in (2) or referee_id is null;
