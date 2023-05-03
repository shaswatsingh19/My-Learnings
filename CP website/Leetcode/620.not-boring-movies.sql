# https://leetcode.com/problems/not-boring-movies/
select *
from cinema
where description <> 'boring' AND id%2 <> 0
ORDER BY rating desc;