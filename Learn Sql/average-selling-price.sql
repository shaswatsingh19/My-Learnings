# https://leetcode.com/problems/average-selling-price
select 
    p.product_id,
    ROUND(sum(units*price)/sum(units),2) as average_price
from prices p
inner join unitssold u
on p.product_id = u.product_id
where purchase_date BETWEEN  start_date AND end_date 
group by p.product_id