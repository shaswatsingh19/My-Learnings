# https://leetcode.com/problems/max-consecutive-ones-ii/submissions/
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i=0
        j=0
        cnt = 0
        m = 0
        check = True
        while j<len(nums):
            if nums[j]==1:
                cnt+=1
            elif nums[j]==0 and check:
                cnt+=1
                check = False
                i = j
            else:
                m = max(m,cnt)
                cnt= j-i
                i=j
            j+=1
                
        m = max(m,cnt)
        return m
        