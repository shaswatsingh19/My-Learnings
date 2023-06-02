# https://leetcode.com/problems/nth-highest-salary
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      select 
        IF(DENSE_RANK() OVER(order by salary DESC)=N,salary,NULL) as getNthHighestSalary
      from employee
      order by getNthHighestSalary DESC
      LIMIT 1
  );
END