# https://leetcode.com/problems/contains-duplicate-ii/
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        di = {}
        for j in range(len(nums)):
            if nums[j] not in di:
                di[nums[j]] = j
            else:
                i = di[nums[j]]
                if abs(j-i)<=k:
                    return True
                di[nums[j]] = abs(j-i)
                
                
        return False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        