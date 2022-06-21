# https://leetcode.com/problems/longest-common-prefix
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        ans = []
        for i in zip(*strs):
            
            if len(set(i))==1:
                ans.append(i[0])
            else:break
                
        return "".join(ans)
    

#         di = {}
#         ans = ''
#         n = len(strs)
        
#         for i in range(len(strs)):
#             string = strs[i]
#             for j in range(len(string)):
                
#                 if string[:j+1] in di:
#                     di[string[:j+1]] += 1
#                 else:
#                     di[string[:j+1]] = 1
                
#                 if di[string[:j+1]] == n and len(string[:j+1])>len(ans):
#                     ans = string[:j+1]         
                
#         return ans
                
                