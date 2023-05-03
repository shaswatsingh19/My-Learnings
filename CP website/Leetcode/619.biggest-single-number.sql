# https://leetcode.com/problems/biggest-single-number/
select max(num) as num
from (
  select num
  from myNumbers
  group by num
  Having count(*) <= 1  
) AS t
