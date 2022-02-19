# https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/
class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        
        if num%3 != 0:
            return []
        
        x = num//3 - 1
        
        return [x,x+1,x+2]