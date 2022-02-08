class Solution:
    def addDigits(self, num: int) -> int:
  
# logic is nice
        if num==0:
            return 0
        else:
            if num%9==0:
                return 9
            else:
                return num%9
        
        
#                 while(num>9):
#                     t = num
#                     s = 0
#                     while(t>0):
#                         r = t%10
#                         s += r
#                         t = t//10

#                     num = s

#                 return num