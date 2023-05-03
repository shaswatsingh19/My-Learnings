# https://leetcode.com/problems/classes-more-than-5-students/
select class
from courses
group by class
having count(*)>=5;