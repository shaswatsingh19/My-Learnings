class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m = 0
        cnt =0
        for i in range(len(nums)):
            if nums[i] == 1:
                cnt+=1
            else:
                m = max(m,cnt)
                cnt = 0
                
                
        m = max(m,cnt)
        return m
        