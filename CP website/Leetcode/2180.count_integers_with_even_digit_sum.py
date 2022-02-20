# https://leetcode.com/problems/count-integers-with-even-digit-sum/
class Solution:
    def countEven(self, num: int) -> int:
        
        cnt = 0
        for i in range(2,num+1,1):
            t  = i
            s = 0
            while(t>0):
                r = t%10
                s += r
                t = t//10
            if s%2==0:
                cnt+=1
                
        return cnt
        