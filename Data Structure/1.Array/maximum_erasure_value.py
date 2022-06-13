# https://leetcode.com/problems/maximum-erasure-value/
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        i = 0
        j = 0
        curr = 0
        maxi = 0
        s = set()
        while j<len(nums):
            if nums[j] not in s:
                s.add(nums[j])
                curr += nums[j]
            else:
                while nums[i]!=nums[j]:# moving i pointer to the next index of nums[j]
                    curr -= nums[i]
                    s.remove(nums[i])
                    i+=1
                    
                i+=1
                
            
            
            maxi = max(maxi,curr)
            j+=1
        return maxi
#         maxi = 0
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)+1):
#                 s = sum(nums[i:j])
#                 if len(nums[i:j]) == len(set(nums[i:j])) and s > maxi:
#                     maxi = s 
        
#         return maxi