# https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/
select customer_number
from orders
group by customer_number
ORDER BY count(*) DESC
LIMIT 1;