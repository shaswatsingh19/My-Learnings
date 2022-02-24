# https://leetcode.com/problems/first-unique-character-in-a-string/
class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        count = collections.Counter(s)
        
        for i in s:
            if count[i] == 1:
                return s.index(i)
        return -1
        
        
#         n = len(s)
#         arr = [0]*26
        
#         ans = 9999999
#         for i in s:
#             ind = ord(i)-97
#             arr[ind] += 1

            
#         ans = 99999999
#         for i in s:
#             ind = ord(i)-97
#             if arr[ind]==1:
#                 ans = min(ans,s.index(i))
        
#         if ans==9999999:
#             return -1
#         return ans
            