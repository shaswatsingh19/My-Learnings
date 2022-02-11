# https://leetcode.com/problems/subarray-sum-equals-k/
class Solution:
    def subarraySum(self, nums: List[int], key: int) -> int:
        

        
        cnt = 0
        di = {0:1}
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            if (s-key) in di:
                cnt += di[s-key]
            
            if s in di:
                di[s] += 1
            else:
                di[s] = 1
        
        return cnt
        
        # O(N*N) time and O(N) space
#         n= len(nums)
#         arr =[0]*(n+1)
#         for i in range(1,n):
#             arr[i] = arr[i-1] + nums[i-1]
#         cnt=0
#         for i in range(n):
#             for j in range(i+1,n+1,1):
#                 print(arr[j]-arr[i])
#                 if(abs(arr[j]-arr[i])== key):
#                     cnt+=1
                    
#         return cnt
        
#         O(N*N*N) time 
#         n = len(nums)
#         cnt =0
#         for i in range(n):
#             for j in range(i,n):
#                 s = 0
#                 for k in range(i,j+1):
#                     s += nums[k]
#                 if s==key:
#                     print(s)
#                     cnt+=1
                    
#         return cnt
                