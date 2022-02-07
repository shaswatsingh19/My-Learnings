# https://leetcode.com/problems/add-binary/
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        # Converting from binary to int and 
        # Add them then
        # convert then using format
#       return '{0:b}'.format(int(a,2)+int(b,2))

        if(a == '0'):return b
        if (b=='0') :return a
        a = self.bin_to_dec(a)
        b = self.bin_to_dec(b)
        ans = a+b
        ans = self.dec_to_bin(ans)
        return ans
        
        
    def bin_to_dec(self,num):
        
        num = int(num)
        i = 0
        dec = 0
        while(num>0):
            r = num%10
            dec = dec + (r*(2**i))
            i+=1
            num= num//10
            
        return dec
        
        
    def dec_to_bin(self,num):
        ans = ''
        while(num>0):
            val = num%2
            ans = str(val) + ans
            num = num//2
            
        return ans