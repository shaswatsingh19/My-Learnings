# https://leetcode.com/problems/excel-sheet-column-number
class Solution:
    def titleToNumber(self, col: str) -> int:
        
        s = 'abcdefghijklmnopqrstuvwxyz'
        col = col.lower()
        di = {}
        
        j=1
        for i in s:
            di[i] = j
            j+=1
            
        j = 0
        res = 0
        for i in range(len(col)-1,-1,-1):
            key = col[i]
            res += di[key]*pow(26,j)
            j+=1
            
        return res
            