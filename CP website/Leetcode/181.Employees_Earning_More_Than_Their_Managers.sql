# https://leetcode.com/problems/employees-earning-more-than-their-managers/
select e.name as Employee
from employee e,employee m
where e.managerId = m.id and e.salary > m.salary;