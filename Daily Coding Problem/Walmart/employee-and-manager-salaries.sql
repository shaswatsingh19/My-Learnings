-- https://platform.stratascratch.com/coding/9894-employee-and-manager-salaries
select 
    e1.first_name,
    e1.salary
from employee e1,employee e2
where e1.manager_id = e2.id AND e1.salary > e2.salary;