# https://leetcode.com/problems/project-employees-i/
select p.project_id,ROUND(avg(e.experience_years),2) as average_years
from project p
inner join employee e
on e.employee_id=p.employee_id
group by project_id;