# https://leetcode.com/problems/the-latest-login-in-2020

# select user_id,MAX(time_stamp) as last_stamp
# from logins
# where YEAR(time_stamp) = 2020
# group by user_id

select 
  DISTINCT user_id,
  FIRST_VALUE(time_stamp) OVER(partition by user_id order by time_stamp DESC) AS last_stamp
from logins
WHERE year(time_stamp) = 2020