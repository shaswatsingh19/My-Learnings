# https://leetcode.com/problems/find-customer-referee
select name
from Customer
where referee_id != 2 OR referee_id is NULL;