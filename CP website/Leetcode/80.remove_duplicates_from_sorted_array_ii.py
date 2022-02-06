# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 0
        n = len(nums)
        temp = n
        while(j<len(nums)):
            if(nums[i]==nums[j]):
                if(j-i>=2):
                    nums.pop(j)
                else:
                    j+=1
            else:
                i=j
                
            
        return len(nums)