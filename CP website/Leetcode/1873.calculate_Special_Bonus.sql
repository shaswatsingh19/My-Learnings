# Write your MySQL query statement below
# https://leetcode.com/problems/calculate-special-bonus/

select employee_id , 
if (employee_id%2= 1 and name not like 'M%',salary,0) as bonus

from Employees;