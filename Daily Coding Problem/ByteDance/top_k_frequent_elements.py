# https://leetcode.com/problems/top-k-frequent-elements/
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        if k==len(nums):
            return nums
        
        #O(N)
        di = {}
        for i in nums:
            if i not in di:
                di[i] = 1
            else:
                di[i] += 1
        ans = heapq.nlargest(k,di.keys(),key = di.get)
        
        return ans
        