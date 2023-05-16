# https://leetcode.com/problems/big-countries
select name,population ,area
from world
where population >= 25000000 OR area >= 3000000;