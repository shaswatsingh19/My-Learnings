# https://leetcode.com/problems/maximum-subarray/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxi = nums[0]
        # initially we think first element is the maximum as if all
        # element are negative and lower than first element
        cur = 0
        
        for i in nums:
            if cur<0:
                cur = 0
            
            cur += i
            
            maxi = max(maxi,cur)
            
        return maxi
            