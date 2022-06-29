# https://leetcode.com/problems/longest-palindrome/
class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        di = {}
        minKey = ''
        minKeyChanged = False
        cnt = 0
        
        di = Counter(s)
                
        for k,v in di.items():
            if v%2 == 1:
                if minKey == '':
                    minKey = k
                elif di[k]< di[minKey]:
                    minKey  = k
                minKeyChanged = True
            
            elif v%2 == 0:
                cnt += v
                
        if minKeyChanged:
            cnt += di[minKey]
            di.pop(minKey)
        
        
        
        for k,v in di.items():
            if v%2 == 1:
                cnt += v - 1
        
        return cnt