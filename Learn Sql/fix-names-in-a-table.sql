# https://leetcode.com/problems/fix-names-in-a-table/
select user_id,CONCAT(UPPER(LEFT(name,1)),LOWER(RIGHT(name,LENGTH(name)-1))) as name
from users
order by user_id