# https://leetcode.com/problems/queries-quality-and-percentage/
select 
  query_name,
  ROUND(avg(rating/position),2) as quality,
  ROUND(avg(CASE WHEN rating<3 THEN 1 ELSE 0 END) * 100,2) as poor_query_percentage  
from queries
group by query_name