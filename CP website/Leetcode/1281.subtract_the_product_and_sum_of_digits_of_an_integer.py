# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        
        s = 0
        p = 1
        
        while n:
            r = n%10
            s+=r
            p*=r
            
            n//=10
            
        return p-s