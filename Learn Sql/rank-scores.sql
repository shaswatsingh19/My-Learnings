# https://leetcode.com/problems/rank-scores/
select
    score,
    DENSE_Rank() OVER(order by score DESC) as 'rank'
FROM scores
order by score desc