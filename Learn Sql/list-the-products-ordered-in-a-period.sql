# https://leetcode.com/problems/list-the-products-ordered-in-a-period
select p.product_name,sum(unit) as unit
from orders
inner join products p
on orders.product_id = p.product_id
where month(order_date) = 2 AND year(order_date) = 2020
group by product_name
having unit >= 100