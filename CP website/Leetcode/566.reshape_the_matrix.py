# https://leetcode.com/problems/reshape-the-matrix/
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:        
        if len(mat)* len(mat[0]) != r*c :
            return mat
    
        ans = [[None for i in range(c)] for j in range(r)]
        print(ans)
            
        cnt = 0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                ans[cnt//c][cnt%c] = mat[i][j]
                cnt+=1
                
        return ans
#         ans = []
#         temp = []
#         cnt = 0
#         for row in mat:
#             for val in row:  
#                 if cnt < c:
#                     temp.append(val)
#                     cnt+=1
#                 else:
#                     ans.append(temp)
#                     temp = [val]
#                     cnt = 1
                    
#         ans.append(temp)
#         return ans



                
        
        