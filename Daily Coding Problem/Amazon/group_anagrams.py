# https://leetcode.com/problems/group-anagrams/
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        di = {}
        for i in strs:
            alp = [0]*26
            
            for c in i:
                alp[ord(c)-97] += 1
            
            if tuple(alp) not in di:
                di[tuple(alp)] = [i]
            else:
                di[tuple(alp)].append(i)
        ans  = []
        for v in di.values():
            ans.append(v)
        return ans
        
#         di = {}
#         for i in range(len(strs)):
#             s = list(strs[i])
#             s.sort()
#             s = "".join(s)
#             if s not in di:
#                 di[s]  = [strs[i]]
#             else:
#                 di[s].append(strs[i])                
#         ans  = []
#         for v in di.values():
#             ans.append(v)
#         return ans

        