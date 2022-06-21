# https://leetcode.com/problems/sort-array-by-parity/
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        o = 0
        e = 0
        while (e<len(nums)):
            if nums[e]%2==0:
                nums[e],nums[o]=nums[o],nums[e]
                o+=1
                e+=1
            else:
                e+=1
                
        return nums