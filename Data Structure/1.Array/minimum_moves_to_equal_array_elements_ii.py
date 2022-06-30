# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        
        nums.sort()
        
        l  = len(nums)
        
        mid = 0
        if l%2==0:
            mid = (nums[l//2] + nums[(l//2) - 1])//2
        else:
            mid = nums[l//2]
        print(mid)
        ans = 0
        for i in nums:
            ans += abs(mid-i)
            
        return ans