# https://leetcode.com/problems/product-sales-analysis-i/
select p.product_name,year,price
from sales s
inner join product p
on s.product_id = p.product_id
ORDER BY p.product_name;