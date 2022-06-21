# https://leetcode.com/problems/single-number/
class Solution:
    def singleNumber(self, arr: List[int]) -> int:
        arr.sort()
        s = 0
        e = len(arr)-1
        
        ans = 0
        while(s<=e):
            if (s==e):
                ans = arr[s]
                break
            mid = (e+s)//2
            if(mid%2==0):
                if(arr[mid]==arr[mid+1]):
                    s =mid+1
                else:
                    e = mid
            else:
                if(arr[mid] == arr[mid+1]):
                    e = mid
                else:
                    s = mid+1
        return ans
        
        
#         ans = 0
#         for i in nums:
#             ans = ans^i
            
#         return ans