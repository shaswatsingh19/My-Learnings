# https://leetcode.com/problems/find-users-with-valid-e-mails/
select * 
from users
where  mail REGEXP "^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode[.]com"