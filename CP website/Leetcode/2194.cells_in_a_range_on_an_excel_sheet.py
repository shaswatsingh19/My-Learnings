# https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/
class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        l = s.split(':')
        print(l)
        
        r1=int(l[0][1])
        r2=int(l[1][1])
        
        c1=l[0][0]
        c2=l[1][0]
        
        print(r1,r2,c1,c2)
        
        res = []
        # r = (ord('c2')-ord('c1')+1)*(r2-r1+1)
        ch = c1
        for i in range(ord(c1),ord(c2)+1):
        
            for j in range(r1,r2+1):
                ans = chr(i)+str(j)
                print(chr(i),str(j))
                res.append(ans)
                
        print(res)
        return res
                
            
            
            