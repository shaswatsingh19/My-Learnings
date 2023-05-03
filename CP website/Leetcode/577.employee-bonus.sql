# https://leetcode.com/problems/employee-bonus/
select name,bonus
from employee e
LEFT JOIN bonus b
on e.empID = b.empID
where bonus < 1000 OR bonus IS NULL;