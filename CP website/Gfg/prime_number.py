# https://practice.geeksforgeeks.org/problems/prime-number2314/1
#User function Template for python3
import math
class Solution:
    def isPrime (self, N):
        if N==1:
            return 0
        
        for i in range(2,math.floor(math.sqrt(N))+1):
            if (N%i == 0):
                return 0
                
                
        return 1
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.isPrime(N))
# } Driver Code Ends