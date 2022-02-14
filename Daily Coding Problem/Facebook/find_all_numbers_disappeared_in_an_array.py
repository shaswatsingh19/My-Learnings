# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        
        arr = [-1]*n
        
        for  i in  range(n):
            arr[nums[i]-1] += 1
            
            
        i = 0
        j = 0
        while(j<n):
            if arr[j] == -1:
                arr[i]  = j+1
                i+=1
            j+=1
            
        return arr[:i]