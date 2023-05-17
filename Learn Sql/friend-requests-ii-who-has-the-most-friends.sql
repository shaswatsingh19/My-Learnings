# https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends
SELECT 
    r as id,
    sum(a) as num 
from
(
    select 
        requester_id as r, count(*) as a
    from requestAccepted
    group by r
UNION ALL
    select 
        accepter_id as r, count(*) as a
    from requestAccepted
    group by r
)aa
group by r
order by num desc
LIMIT 1