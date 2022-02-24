# https://leetcode.com/problems/ransom-note/
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        
        count = collections.Counter(ransomNote)
        # mag = collections.Counter(magazine)
        
        for i in magazine:
            if count[i]>0:
                count[i]-=1
                
        for i in count:
            if count[i]>0:
                return False
                
        return True