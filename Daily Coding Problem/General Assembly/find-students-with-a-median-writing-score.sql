-- https://platform.stratascratch.com/coding/9610-find-students-with-a-median-writing-score
WITH cte1 AS (select 
    student_id,
    sat_writing,
    rank() OVER(order by sat_writing) as ranking
from sat_scores),
cte2 AS (SELECT FLOOR(COUNT(*)/2) AS median_number from sat_scores)

SELECT student_id
FROM cte1
JOIN cte2
ON cte1.ranking = cte2.median_number