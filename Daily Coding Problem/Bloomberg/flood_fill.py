# https://leetcode.com/problems/flood-fill/
from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        # BFS
        
        R = len(image)
        C = len(image[0])
        old_color = image[sr][sc]
        
        if old_color == color :
            return image
        q = deque()
        
        i = sr
        j = sc
        
        q.append((i,j))
        
        
        while q:
            i,j = q.popleft()
            if i<0 or i>=R or j<0 or j>=C or image[i][j] != old_color:
                continue 
            
            if image[i][j] == old_color:
                image[i][j] = color
                q.append((i+1,j))
                q.append((i-1,j))
                q.append((i,j+1))
                q.append((i,j-1))
                
        return image
                
        

        
        
#         row = len(image)
#         col = len(image[0])
        
#         old_color = image[sr][sc]
        
#         if image[sr][sc] == color:
#             return image
        
#         def dfs(i,j):
#             if (i<0 or i>=row ) or (j<0 or j>=col):
#                 return 
#             elif image[i][j] == old_color:
#                 image[i][j] = color
#                 dfs(i+1,j)
#                 dfs(i-1,j)
#                 dfs(i,j+1)
#                 dfs(i,j-1)
                
#         dfs(sr,sc)
#         return image
        
        
        
        
        