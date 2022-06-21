# https://leetcode.com/problems/power-of-three/
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        if n==0:
            return False
        if n==3 or n==1:
            return True
        
        if n%3==0:
            return self.isPowerOfThree(n//3)
        
        
        