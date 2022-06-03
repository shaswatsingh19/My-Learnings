# https://leetcode.com/problems/range-sum-query-2d-immutable/
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.mat = matrix
        temp  = 0
        for i in range(len(self.mat)):
            self.mat[i][0] += temp
            for j in range(1,len(self.mat[0])):
                self.mat[i][j] += self.mat[i][j-1]
                if j == len(self.mat[0])-1:
                    temp = self.mat[i][j]# 10
        print(self.mat)
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        cnt = 0
        
        
        for i in range(row1,row2+1):
            cnt += self.mat[i][col2] 
            if col1-1 > -1:
                cnt -= self.mat[i][col1-1]

                
        return cnt

    
    
#         for i in range(row1,row2+1):
#             for j in range(col1,col2+1):
#                 # print(self.mat[i][j])
                
#                 cnt += self.mat[i][j]


# for i in range(row1,row2+1):
#     cnt += sum(self.mat[i][col1:col2+1])
# print(cnt)
# return cnt
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)