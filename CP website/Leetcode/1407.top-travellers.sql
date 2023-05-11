# https://leetcode.com/problems/top-travellers
select 
  u.name as name,
  CASE
    WHEN r.distance IS NOT NULL THEN  sum(r.distance) 
    ELSE 0
  END AS travelled_distance
from users u
left join rides r
on u.id = r.user_id
group by u.id,u.name
order by travelled_distance DESC,name