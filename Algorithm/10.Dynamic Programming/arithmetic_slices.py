# https://leetcode.com/problems/arithmetic-slices/
class Solution:
    def numberOfArithmeticSlices(self, arr: List[int]) -> int:
        
        if len(arr)<3:
            return 0
        f = arr[0]
        s = arr[1]
        arr[0]=0
        arr[1]=0
        ans = 0
        for i in range(2,len(arr)):
            t = arr[i]
            if t-s==s-f:
                arr[i] = arr[i-1]+1
                ans += arr[i]
            else:
                arr[i] = 0
                
            f = s
            s = t
        
        return ans

#         arr = [0]*len(nums)
        
#         ans = 0
#         for i in range(2,len(nums)):
#             if nums[i]-nums[i-1] == nums[i-1]-nums[i-2]:
#                 arr[i] = arr[i-1] + 1
#                 ans += arr[i]
                
#         return ans
