# https://leetcode.com/problems/bank-account-summary-ii/
select name AS NAME,sum(t.amount) AS BALANCE
from users u
inner join transactions t
on u.account = t.account
group by t.account
having sum(t.amount) > 10000