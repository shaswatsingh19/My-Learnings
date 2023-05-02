-- https://datalemur.com/questions/laptop-mobile-viewership
-- SELECT 
--   SUM(CASE WHEN device_type ='laptop' THEN 1 ELSE 0 END) AS laptop,
--   SUM(CASE WHEN device_type IN ('tablet','phone') THEN 1 ELSE 0 END) AS mobile
-- FROM viewership;

SELECT
  count(*) FILTER (WHERE device_type = 'laptop') AS laptop,
  count(*) FILTER (WHERE device_type = 'tablet' OR device_type='phone') AS mobile
FROM viewership;


