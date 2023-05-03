# https://leetcode.com/problems/swap-salary

# update salary 
# SET sex = IF (sex='m','f','m')

update salary
set sex = CASE
  WHEN sex= 'm' THEN 'f'
  ELSE 'm'
END;