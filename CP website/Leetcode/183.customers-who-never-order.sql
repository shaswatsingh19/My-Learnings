# https://leetcode.com/problems/customers-who-never-order/description

select name as Customers
from Customers
WHERE id NOT IN (
    select customerID as id
    from orders
)