# https://leetcode.com/problems/rising-temperature/
SELECT w1.id
FROM Weather w1,Weather w2 
where w1.recordDate = w2.recordDate + INTERVAL 1 DAY
AND w1.temperature > w2.temperature;
