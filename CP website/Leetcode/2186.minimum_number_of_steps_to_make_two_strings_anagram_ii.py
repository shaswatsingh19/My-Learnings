# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram-ii
class Solution:
    def minSteps(self, c: str, t: str) -> int:
        dd = Counter(t)
        
        cnt=0
        
        for i in c:
            if dd[i]>0:
                dd[i]-=1
            else:
                cnt+=1
        for i in dd:
            cnt+=dd[i]
            
        return cnt