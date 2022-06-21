# https://leetcode.com/problems/missing-number/
class Solution:
    
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        s = (n*(n+1))//2
        
        sum_num = sum(nums)
        
        return s-sum_num