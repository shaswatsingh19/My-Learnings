# https://leetcode.com/problems/valid-anagram/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
#         return collections.Counter(s)==collections.Counter(t)
        
        count = collections.Counter(s)
        
        for i in t:
            if i in count:
                count[i] -=1
            else:
                return False
            
        for i in count:
            if count[i]>0:
                return False
            
        return True
    
    
