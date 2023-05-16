# https://leetcode.com/problems/exchange-seats/
select 
  CASE 
    WHEN ((id%2 = 1) AND ( id = (select count(*) from seat))) THEN id
    WHEN id%2 = 1 THEN id+1
    ELSE id-1
  END AS id,
  student
from seat
order by id