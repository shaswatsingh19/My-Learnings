# https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/
select u.unique_id,e.name
from employees e
left join employeeUNI u
ON e.id = u.id;