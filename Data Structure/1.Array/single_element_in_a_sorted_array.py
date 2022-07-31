# https://leetcode.com/problems/single-element-in-a-sorted-array/
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        l = 0
        h = len(nums)-1
        
        while l<h:
            mid = (l+h)//2
            
            if mid % 2==0:
                if nums[mid] == nums[mid+1]:
                    l = mid+1
                else:
                    h = mid
            else:
                if nums[mid] == nums[mid+1]:
                    h = mid
                else:
                    l = mid+1
                    
                    
        return nums[l]
        
        # reduce is a function that perform a function on a iterator
        # here we perform xor on nums
        # return reduce(xor,nums)