# https://leetcode.com/problems/movie-rating
(select name as results
from users u
inner join movieRating mr
on u.user_id = mr.user_id
group by u.user_id
order by count(*) DESC,results
LIMIT 1)
UNION all
(select title as results
from movies m
inner join movieRating mr
on m.movie_id = mr.movie_id
where date_format(created_at,'%Y-%m') = '2020-02'
group by m.movie_id
order by avg(rating) DESC,results 
LIMIT 1)