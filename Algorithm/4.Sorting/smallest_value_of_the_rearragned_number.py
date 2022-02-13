# https://leetcode.com/problems/smallest-value-of-the-rearranged-number/
class Solution:
    def smallestNumber(self, num: int) -> int:
        
        str_num = str(abs(num))
        
        str_num = list(str_num)
        
        if num>0:
            str_num.sort()
            i= 0
            while(str_num[i]=='0'):
                i+=1
            temp = str_num[0]
            str_num[0] = str_num[i]
            str_num[i] = temp
    
        else:
            str_num.sort(reverse=True)
            
        new_num = int("".join(str_num))
    
        
        if num<0:
            new_num *= -1
            
        return new_num