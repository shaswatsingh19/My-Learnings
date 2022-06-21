# https://leetcode.com/problems/transpose-matrix/solution/
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        ans = []
        for j in range(len(matrix[0])):
            arr = []
            for i in range(len(matrix)):
                arr.append(matrix[i][j])
            ans.append(arr)
            
        return (ans)