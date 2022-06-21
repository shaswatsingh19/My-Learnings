# https://leetcode.com/problems/third-maximum-number
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        f,s,t = -2**31-1,-2**31-1,-2**31-1
        
        for i in nums:
            if i>f:
                t,s,f=s,f,i
            elif i>s and i!=f :
                t,s=s,i
            elif i>t and i!=s and i!=f:
                t=i
                
        if t==-2**31-1:
            return f
        return t