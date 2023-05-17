# https://leetcode.com/problems/department-highest-salary
select 
    department,employee,salary 
from (
    select 
        d.name as department,
        e.name as employee,
        salary,
        RANK() OVER(partition by departmentID order by salary desc ) as rk
    FROM employee e
    inner join department d
    on e.departmentID = d.id)a
where rk=1