-- https://platform.stratascratch.com/coding/9897-highest-salary-in-department
select 
    department,
    first_name,
    salary
from employee
where (department,salary) IN (
    select department,MAX(salary) from employee group by department
    )