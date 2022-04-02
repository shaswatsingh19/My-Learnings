# https://leetcode.com/problems/search-insert-position/
class Solution:
    def searchInsert(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        ans = -1
        s = 0
        e = n-1
        
        while(s<=e):
            mid = s + (e-s)//2
            if(k<=nums[mid]):
                ans = mid
                e = mid-1
                
            else:
                s = mid +1
                ans = mid+1
                
        return ans
        
        