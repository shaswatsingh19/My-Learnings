# https://leetcode.com/problems/counting-bits/
class Solution:
    def countBits(self, n: int) -> List[int]:
        
        dp = [0]*(n+1)
        minus = 0
        j = 0
        for i in range(1,n+1):
            
            if i ==pow(2,j):
                j+=1
                minus = i
                
            dp[i] = 1 + dp[i-minus]
            
        return dp
            
#         arr = [0]*(n+1)
        
        
#         i = 1
#         while i<=n:
#             temp = i
#             cnt = 0
#             while temp:
#                 cnt+=1
#                 temp = temp&(temp-1)
                
                
#             arr[i] = cnt
#             i+=1
            
#         return arr
            
        