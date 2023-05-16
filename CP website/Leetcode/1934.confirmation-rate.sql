# https://leetcode.com/problems/confirmation-rate
select 
  s.user_id,
  ROUND(((SUM(CASE 
    WHEN action = 'confirmed' THEN 1 ELSE 0
  END))/IF(count(action),count(action),1)),2)  AS confirmation_rate
from signups s
left join confirmations c
on s.user_id = c.user_id
group by s.user_id