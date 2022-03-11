# https://leetcode.com/problems/product-of-array-except-self/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        multi = 1
        zero_count = 0
        for i in nums:
            if i != 0:
                multi = multi * i
            else:
                zero_count  += 1

        for i in range(len(nums)):
            if zero_count > 1:
                nums[i] = 0
            elif zero_count == 1:
                nums[i] = 0 if nums[i]!=0 else multi
            else:
                nums[i] = multi//nums[i]
            
        return nums