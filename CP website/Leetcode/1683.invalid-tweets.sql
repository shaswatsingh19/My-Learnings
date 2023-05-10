# https://leetcode.com/problems/invalid-tweets
select tweet_id
from tweets
where length(content)>15;