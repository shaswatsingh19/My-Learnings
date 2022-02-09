# https://leetcode.com/problems/k-diff-pairs-in-an-array/
class Solution:
    def findPairs(self, nums: List[int], key: int) -> int:
        
        di ={}
        cnt = 0
        for i in range(len(nums)):
            if nums[i] not in di:
                di[nums[i]] = 1
            else:
                di[nums[i]] += 1
                    
        if key==0:
            for k,v in di.items():
                if v>1:
                    cnt+=1
        else:
            for k,v in di.items():
                if (k + key) in di:
                    cnt+=1
                    

                
        print(di)
        return cnt