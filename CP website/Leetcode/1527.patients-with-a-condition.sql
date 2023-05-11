# https://leetcode.com/problems/patients-with-a-condition/
select * from patients
where conditions LIKE "% DIAB1%" OR conditions LIKE "DIAB1%"