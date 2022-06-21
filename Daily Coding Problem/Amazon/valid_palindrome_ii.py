# https://leetcode.com/problems/valid-palindrome-ii
class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def palindromeCheck(s,l,h):
            while (l<h):
                if s[l] != s[h]:
                    return False
                l+=1
                h-=1
                
            return True
        
        
        l = 0
        h = len(s)-1
        
        while l<h:
            if s[l] != s[h] :
                return ( palindromeCheck(s,l+1,h) or palindromeCheck(s,l,h-1) )
            l+=1
            h-=1
        return True
                
    
        