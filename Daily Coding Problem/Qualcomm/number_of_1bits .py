# https://leetcode.com/problems/number-of-1-bits/
class Solution:
    def hammingWeight(self, n: int) -> int:
        
        cnt = 0
        while n:
            n = n&(n-1) # remove least significant bit fastly
            cnt+=1
            
        return cnt
        # cnt=0
        # while n:
        #     cnt += n&1
        #     n = n>>1
        # return cnt
        