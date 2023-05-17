# https://leetcode.com/problems/immediate-food-delivery-ii/
select 
  ROUND((SUM(IF(order_date = customer_pref_delivery_date,1,0))*100) / count(DISTINCT customer_id) ,2) as immediate_percentage
from delivery
where (customer_id , order_date) IN (
  select customer_id , min(order_Date)  as min_date
  from delivery 
  group by customer_id)