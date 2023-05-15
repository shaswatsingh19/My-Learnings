# https://leetcode.com/problems/last-person-to-fit-in-the-bus
select person_name
FROM (
  select 
    *,
    SUM(weight) OVER(order by turn rows between unbounded preceding AND current row) as running_total
  from Queue)a
WHERE running_total <= 1000
order by turn desc
LIMIT 1