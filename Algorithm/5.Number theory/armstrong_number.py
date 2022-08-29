# https://leetcode.com/problems/armstrong-number/solution/
class Solution:
    def isArmstrong(self, n: int) -> bool:
        l = 0
        temp = n
        res = 0
        while temp:
            rem = temp%10
            l+=1
            temp = temp//10
        
        temp = n
        while temp:
            rem = temp%10
            res += pow(rem,l)
            temp = temp//10
            
        if res==n:
            return True
        return False