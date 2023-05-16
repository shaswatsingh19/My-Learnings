# https://leetcode.com/problems/customers-who-bought-all-products

# select customer_id
# FROM (select DISTINCT *
# from customer )a
# group by customer_id
# having count(product_key) = (select count(*) from product)
# order by customer_id


select customer_id
from customer 
group by customer_id
having count(DISTINCT product_key) = (select count(*) from product)