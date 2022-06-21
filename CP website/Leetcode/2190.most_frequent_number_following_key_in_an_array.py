# https://leetcode.com/problems/most-frequent-number-following-key-in-an-array/
class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        di = {}
        for i in range(1,len(nums)):
            if nums[i-1] == key:
                if nums[i] not in di:
                    di[nums[i]] = 1
                else:
                    di[nums[i]] += 1
                    
                    
        print(di)
        
        maxi = 0
        key = 0
        for k,v in di.items():
            if v>maxi:
                maxi = v
                key = k
                print(k,v)
                
        return key