# https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/
select 
    *
from employees e 
join employees m
on e.reports_to = m.employee_id