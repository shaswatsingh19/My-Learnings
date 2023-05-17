# https://leetcode.com/problems/product-sales-analysis-iii
select 
    product_id,
    year as first_year,
    quantity,
    price
FROM(select 
    *,
    RANK() OVER(partition by product_id order by year) as o
from sales)a
where o=1