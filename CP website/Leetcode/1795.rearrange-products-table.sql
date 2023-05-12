# https://leetcode.com/problems/rearrange-products-table/
select 
  product_id,
  'store1' as store,
  store1 as price 
from products
where store1 IS NOT NULL
UNION
select 
  product_id,
  'store2' as store,
  store2 as price 
from products
where store2 IS NOT NULL
UNION
select 
  product_id,
  'store3' as store,
  store3 as price 
from products
where store3 IS NOT NULL