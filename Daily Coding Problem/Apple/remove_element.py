# https://leetcode.com/problems/remove-element/
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        i = 0
        j = len(nums)-1
        
        while(i<=j):
            if nums[i] == val and nums[j]!= val:
                nums[i],nums[j]  = nums[j] , nums[i]
                i+=1
                j-=1
            elif nums[i] == val and nums[j] == val:
                j-=1
            else:
                i+=1
                
        return i
        