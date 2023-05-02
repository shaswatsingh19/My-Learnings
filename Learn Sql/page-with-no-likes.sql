-- https://datalemur.com/questions/sql-page-with-no-likes
SELECT page_id from pages
WHERE page_id NOT IN (SELECT page_id from page_likes);