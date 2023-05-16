# https://leetcode.com/problems/monthly-transactions-i
select 
    # CONCAT(year(trans_date),"-",if(month(trans_date)<10,concat('0',month(trans_date)),month(trans_date))) as month,
    date_format(trans_date,"%Y-%m") as month,
    country,
    count(*) as trans_count,
    SUM(IF(state='approved',1,0)) as approved_count,
    sum(amount) as trans_total_amount,
    SUM(IF(state='approved',amount,0)) as approved_total_amount
from transactions
group by month,country