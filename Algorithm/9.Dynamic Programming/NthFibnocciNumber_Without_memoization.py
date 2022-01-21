# https://www.codingninjas.com/codestudio/guided-paths/basics-of-python/content/118792/offering/1461393
def fibonacciNumber(n):
    # Write your code here.
    
#     memo = [0]*(n+1)
# 	  memo[1] = 1    
    mod = int(1e9+7)
    a = 0
    b = 1
    for i in range(2,n+1):
        c = (a+b)%mod
        a = b
        b = c
        
#         if(memo[i]==0):
#             memo[i] = (memo[i-1]+memo[i-2])%mod
		
#     return memo[n
    return b
    
# O(N) O(1)