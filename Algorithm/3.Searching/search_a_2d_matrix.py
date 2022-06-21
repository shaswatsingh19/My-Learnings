# https://leetcode.com/problems/search-a-2d-matrix/
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

# Think of an imaginary array         
        m = len(matrix)
        n = len(matrix[0])
        
        l = 0
        r = m*n -1 
        
        while(l<=r):
            mid = (l+r)//2
            if matrix[mid//n][mid%n]==target:
                return True
            elif matrix[mid//n][mid%n] > target:
                r = mid-1
            else:
                l = mid+1
        return False        



#  ---------------------------------------------------------------------

#         r = len(matrix)
#         c = len(matrix[0])
        
#         i = 0
#         j = c-1
        
#         while(i<r and j>-1):
#             if matrix[i][j] == target:
#                 return True
            
#             elif matrix[i][j] < target:
#                 i+=1
#             else:
#                 j-=1
                
#         return False
        

        


# -----------------------------------------------------
    
#         r = len(matrix)
#         c = len(matrix[0])
        
#         for i in range(r):
            
#             if matrix[i][0]<=target and target<= matrix[i][c-1]:
                
#                 s = 0
#                 e = c-1
                
#                 while(s<=e):
#                     mid = (s+e)//2
#                     if matrix[i][mid] == target:
#                         return True
#                     elif matrix[i][mid] > target:
#                         e = mid-1
#                     else:
#                         s = mid+1
#         return False                
        
# --------------------------------------------------------------------------------


#         m = len(matrix)
#         n = len(matrix[0])
        
#         for i in range(m):
#             for j in range(n):
#                 if matrix[i][j] == target:
#                     return True
                    
#         return False