# https://leetcode.com/problems/pascals-triangle/
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        ans = []
        
        for i in range(numRows):
            temp = [0]*(i+1)
            temp[0]  = 1
            temp[len(temp)-1] = 1
            
            for j in range(1,len(temp)-1):
                temp[j] = ans[i-1][j-1] + ans[i-1][j]
                
            ans.append(temp)
        
        return ans