# https://leetcode.com/problems/average-time-of-process-per-machine
select 
    machine_id,
    ROUND((SUM(CASE 
        WHEN activity_type = 'end' THEN timestamp
        ELSE 0
    END ) - SUM(CASE 
        WHEN activity_type = 'start' THEN timestamp
        ELSE 0
    END))/count(DISTINCT process_id),3) as processing_time
FROM activity
group by machine_id