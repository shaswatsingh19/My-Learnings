# https://leetcode.com/problems/majority-element/
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        
        maxi = None
        cnt = 0
        
        for el in nums:
            if cnt==0:
                maxi = el
                
            cnt += (1 if el==maxi else -1)
            
            
        return maxi