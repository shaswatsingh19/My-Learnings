# https://leetcode.com/problems/single-number/
class Solution:
    def singleNumber(self, arr: List[int]) -> int:
        
        ans = 0
        for i in nums:
            ans = ans^i
            
        return ans