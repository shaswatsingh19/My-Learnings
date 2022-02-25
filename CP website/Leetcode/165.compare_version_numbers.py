# https://leetcode.com/problems/compare-version-numbers/
class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        
#         t1 = list(map(int,v1.split('.')))
#         t2 = list(map(int,v2.split('.')))
        
        
#         if len(t1)<len(t2):
#             a  = [0]*(len(t2)-len(t1))
#             t1.extend(a)
#         else:
#             a  = [0]*(len(t1)-len(t2))
#             t2.extend(a)
        
        
#         for i in range(len(t1)):
#             val1 = t1[i]
#             val2 = t2[i]
            
#             if val1 == val2 :
#                 continue 
                
#             return -1 if val1<val2 else 1
            
#         return 0
        
        
        t1 = list(map(int,v1.split('.')))
        t2 = list(map(int,v2.split('.')))
        
        for i,j in zip_longest(t1,t2,fillvalue=0):
            if i==j:
                continue
                
            return -1 if i<j else 1
        
        return 0