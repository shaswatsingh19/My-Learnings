# https://leetcode.com/problems/count-salary-categories/
select 
    'Low Salary' as category,
    SUM(CASE WHEN income<20000 THEN 1 ELSE 0 end ) as accounts_count
FROM accounts
UNION
select 
    'Average Salary' as category,
    SUM(CASE WHEN income>=20000 AND income<=50000 THEN 1 ELSE 0 end ) as accounts_count
FROM accounts
UNION
select 
    'High Salary' as category,
    SUM(CASE WHEN income>50000 THEN 1 ELSE 0 end ) as accounts_count
FROM accounts
