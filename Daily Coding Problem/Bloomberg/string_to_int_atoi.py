# https://leetcode.com/problems/string-to-integer-atoi/
class Solution:
    def myAtoi(self, s: str) -> int:
        
        if(len(s)==0):
            return 0
        ans = 0
        pos = True
        i = 0
        
        while(i<len(s) and s[i] == ' '):
            i+=1
            
        if (i<len(s) and s[i] == "+"):
            pos = True
            i+=1
        elif (i<len(s) and s[i] == '-'):
            pos = False
            i+=1
            
        if i<len(s) and s[i]>='0' and s[i]<='9':
            while(i<len(s) and s[i]>='0' and s[i]<='9' ):
                ans = ans*10 + int(s[i])
                i+=1
                
            if (pos == False):
                ans = ans*-1
            
            if(ans<-pow(2,31)):
                    return -pow(2,31)
            
            if (ans>pow(2,31)-1):
                return pow(2,31)-1

            
            
            
        return ans