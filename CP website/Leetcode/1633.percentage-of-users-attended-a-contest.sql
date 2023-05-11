# https://leetcode.com/problems/percentage-of-users-attended-a-contest
select 
  contest_id,
  ROUND((parti/(select count(user_id) from users) )*100,2) as percentage from
(select 
  contest_id,
  count(*) as parti
from register 
group by contest_id
)aa
order by percentage DESC,contest_id


# ROUND(COUNT(user_id) / (SELECT COUNT(user_id) FROM users) * 100, 2) AS percentage