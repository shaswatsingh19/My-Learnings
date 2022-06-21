# https://leetcode.com/problems/contains-duplicate/
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        di = {}
        
        for i in nums:
            if i not in di:
                di[i] = 1
            else:
                return True
            
        return False

#       return len(nums) != len(set(nums))