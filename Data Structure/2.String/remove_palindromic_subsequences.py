# https://leetcode.com/problems/remove-palindromic-subsequences
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        
        
        if(self.ispalindrome(s)):
            return 1
        else:
            return 2
        
    def ispalindrome(self,st):
        s = 0
        e = len(st)-1
        while s<e:
            if st[s] != st[e]:
                return False
            s+=1
            e-=1
            
        return True