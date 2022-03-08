# https://leetcode.com/problems/find-pivot-index/
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        s = sum(nums)
        l=0
        for i in range(len(nums)):
            
            p = i
            r = s - l - nums[p]
            if r == l:
                return p
            l =l+ nums[p]
            
            
            
        return -1
        