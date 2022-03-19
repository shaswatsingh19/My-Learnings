# https://leetcode.com/problems/isomorphic-strings/solution/
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        s1 = set(s)
        s2 = set(t)
        
        if len(s1)!=len(s2):
            return False
        
        ans = ''
        di = {}
        i = 0
        while i<len(s):
            di[s[i]] = t[i]
            i+=1
            
        for i in range(len(s)):
            if di[s[i]] != t[i]:
                return False
        
        return True
            
        