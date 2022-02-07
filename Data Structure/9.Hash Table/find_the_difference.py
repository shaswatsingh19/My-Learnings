# https://leetcode.com/problems/find-the-difference/
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        asc_s = 0
        asc_t = 0
        for i in s:
            asc_s += ord(i)
            
        for i in t:
            asc_t += ord(i)
            
        res = asc_t - asc_s
        
        return chr(res)

#             di ={}
#             for i in t:
#                 if i not in di:
#                     di[i] = 1
#                 else:
#                     di[i] += 1

#             for i in s:
#                 if i in di:
#                     di[i] -= 1


#             for k,v in di.items():
#                 if v>0:
#                     ans = k
#                     break

#             return ans

