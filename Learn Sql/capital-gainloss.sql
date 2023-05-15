# https://leetcode.com/problems/capital-gainloss
# select 
#     stock_name,
#     SUM(
#         CASE 
#             WHEN operation = 'sell' THEN price ELSE 0
#         END
#     ) - SUM(
#         CASE 
#             WHEN operation = 'buy' THEN price ELSE 0
#         END
#     )as capital_gain_loss
# FROM stocks
# group by stock_name

select 
    stock_name,
    SUM(if(operation='buy',-price,price)) AS capital_gain_loss
FROM stocks
group by stock_name