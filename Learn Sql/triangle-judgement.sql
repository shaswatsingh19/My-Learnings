# https://leetcode.com/problems/triangle-judgement/
select x,y,z,
    CASE
        WHEN (x+y<=z OR x+z<=y OR y+z<=x) THEN 'No'
        ELSE 'Yes'
    END AS "triangle"
FROM triangle;