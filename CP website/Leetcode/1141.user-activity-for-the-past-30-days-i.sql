# https://leetcode.com/problems/user-activity-for-the-past-30-days-i
select  activity_date as day,count(DISTINCT user_id) as active_users
from activity
where activity_date between ADDDATE("2019-07-27",INTERVAL -29 DAY) AND "2019-07-27"
group by activity_date