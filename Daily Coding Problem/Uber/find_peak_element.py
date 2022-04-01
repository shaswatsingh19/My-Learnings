# https://leetcode.com/problems/find-peak-element/
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        curr=0
        
        low = 0
        high = len(nums)-1
        while (low<high):
            mid = (low+high)//2
            if nums[mid]<nums[mid+1]:
                curr = mid+1
                low = mid+1
            else:
                high  = mid
        
        if len(nums)>1 and nums[mid]<nums[mid+1]:
            curr = mid+1
        return curr
                
        