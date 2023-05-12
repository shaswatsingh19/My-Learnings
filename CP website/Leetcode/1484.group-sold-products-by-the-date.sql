# https://leetcode.com/problems/group-sold-products-by-the-date/
select 
  sell_date,
  count(DISTINCT product) AS num_sold,
  GROUP_CONCAT(DISTINCT product order by product) as products
from activities 
group by sell_date