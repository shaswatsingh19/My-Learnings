# https://leetcode.com/problems/restaurant-growth/
select 
    DISTINCT visited_on,amount,ROUND(amount/7,2) as average_amount
FROM (
    select 
        visited_on,
        SUM(amount) OVER (order by visited_on range between interval 6 day preceding AND current row ) as amount,
        DENSE_rank() oVer(order by visited_on) as rk
    from customer
)a
where rk>=7
