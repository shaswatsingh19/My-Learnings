# https://leetcode.com/problems/subsets/
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        n  = len(nums)
        
        return self.sub(0,[],[],n,nums)
    
    
    
    def sub(self,i,l,new_a,n,nums):
        if i>=n:
            temp = l.copy()
            new_a.append(temp)
            return 

        l.append(nums[i])
        self.sub(i+1,l,new_a,n,nums)
        l.remove(nums[i])
        self.sub(i+1,l,new_a,n,nums)

        return new_a

    