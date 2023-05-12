# https://leetcode.com/problems/primary-department-for-each-employee
select employee_id,department_id
from employee
GROUP by employee_id
having count(*)=1
UNION
select employee_id,department_id
from employee
where primary_flag = 'Y'