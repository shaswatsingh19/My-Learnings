-- https://platform.stratascratch.com/coding/9782-customer-revenue-in-march
select 
    cust_id,
    sum(total_order_cost) as revenue
FROM orders
where EXTRACT(year from order_date) = 2019 AND   EXTRACT(month from order_date) = 03
group by cust_id
order by revenue desc