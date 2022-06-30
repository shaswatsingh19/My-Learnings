# https://leetcode.com/problems/backspace-string-compare/
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ans = ''
        
        cnt = 0
        
        def solution(st):
            ans = ''
            cnt = 0
            for i in range(len(st)-1,-1,-1):

                if cnt and st[i] !='#':
                    cnt-=1
                    continue

                if st[i] != '#':
                    ans = st[i] + ans
                else:
                    cnt+=1
            return ans
                  
        ansS = solution(s)
        ansT = solution(t)
        return ansS == ansT
    
    
        
#         s1  = []
#         s2  = []
        
#         for i in s:
#             if not s1 and i=='#':
#                 continue
#             if i != '#':
#                 s1.append(i)
#             else:
#                 s1.pop()
                
        
#         for i in t:
#             if not s2 and i=='#':
#                 continue
#             if i != '#':
#                 s2.append(i)
#             else:
#                 s2.pop()
                
#         return s1==s2
                