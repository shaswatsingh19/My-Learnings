# https://leetcode.com/problems/second-highest-salary/
select 
  IF(DENSE_RANK() OVER(order by salary DESC)=2,salary,NULL) as SecondHighestSalary
from employee
order by SecondHighestSalary DESC
LIMIT 1