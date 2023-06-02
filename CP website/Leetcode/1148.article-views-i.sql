# https://leetcode.com/problems/article-views-i
select DISTINCT author_id as id from views
where author_id = viewer_id
ORDER By author_id;