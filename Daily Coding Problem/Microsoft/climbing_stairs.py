# https://leetcode.com/problems/climbing-stairs/
class Solution:
    def climbStairs(self, n: int) -> int:
        
        f =0
        s =1
        c=0
        i= c
        if n==1:
            return 1
        
        while(i<n):
            c = f+s
            f =s
            s = c
            
            i+=1
            
        return c