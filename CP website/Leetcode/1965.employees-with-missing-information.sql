# https://leetcode.com/problems/employees-with-missing-information
select employee_id from 
(select e.employee_id,e.name
from employees e
UNION
select s.employee_id,s.salary
from salaries s)a
group by employee_id
having count(*)<2
order by employee_id