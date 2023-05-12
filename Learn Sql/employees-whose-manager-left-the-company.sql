# https://leetcode.com/problems/employees-whose-manager-left-the-company/
select 
employee_id
from employees
WHERE manager_id NOT IN (
select employee_id from employees) AND salary < 30000
order by employee_id