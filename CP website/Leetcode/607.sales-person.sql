# https://leetcode.com/problems/sales-person/
SELECT name 
from Salesperson
WHERE sales_id NOT IN (
  SELECT sales_id
  from orders
  WHERE com_id IN (
    select com_id 
    from company
    where name = 'RED'
  )
)