-- https://platform.stratascratch.com/coding/9917-average-salaries
select 
    department,
    first_name,salary,
    avg(salary) over(partition by department) as avg_Sal
from employee