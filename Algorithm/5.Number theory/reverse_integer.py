# https://leetcode.com/problems/reverse-integer/
class Solution:
    def reverse(self, x: int) -> int:
        
        
        isPos = True
        if (x<0):
            isPos = False
            x = abs(x)
        rev = []
        temp = x
        l = 0
        while temp:
            rem = temp%10
            rev.append(rem)
            l+=1
            temp = temp//10
            
        ans = 0
        for i in rev:
            ans += 10**(l-1) * i
            l-=1
        
        if (isPos == False):
            ans = ans*-1
            
        if (ans> pow(2,31)-1 or ans< -pow(2,31)):
            return 0
        return ans