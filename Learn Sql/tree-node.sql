# https://leetcode.com/problems/tree-node
# select 
#     id,'Root' as type
# FROM tree
# WHERE 
#     p_id IS NULL
# UNION
# select id,'Inner' as type
# from tree
# where 
#     p_id IS NOT NULL 
#     AND id IN (
#         select DISTINCT p_id
#         from tree
#         where p_id IS NOT NULL)
# UNION
# select 
#     id,'Leaf' as type
# FROM tree
# WHERE 
#     id NOT IN (select 
#                     DISTINCT p_id from tree 
#                     where p_id is NOT NULL) 
#                 AND p_id IS NOT NULL


select 
    id,
    CASE
        WHEN p_id is NULL THEN 'Root' 
        WHEN id NOT IN (Select DISTINCT p_id from tree where p_id IS NOT NULL) THEN 'Leaf'
        ELSE 'Inner'
    END as type
from tree



