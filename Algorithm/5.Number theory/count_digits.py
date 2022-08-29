#User function Template for python3
# https://practice.geeksforgeeks.org/problems/count-digits5716/1

class Solution:
    def evenlyDivides (self, N):
        temp = N
        cnt = 0
        while temp:
            rem = temp%10
            if (rem!= 0 and N%rem== 0):cnt+=1
            temp = temp//10
            
        return cnt
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.evenlyDivides(N))
# } Driver Code Ends