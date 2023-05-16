# https://leetcode.com/problems/managers-with-at-least-5-direct-reports
select name from 
employee 
WHERE id IN (select managerId
from employee
where managerId IS NOT NULL
group by managerId
having count(*) >= 5)