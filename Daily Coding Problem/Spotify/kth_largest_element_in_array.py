# https://leetcode.com/problems/kth-largest-element-in-an-array/
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # return heapq.nlargest(k, nums)[-1]
        kArr = []
        
        for i in range(len(nums)):
            if len(kArr)<k:
                kArr.append(nums[i])
                
            else:
                kArr.sort(reverse = True)
                if kArr[-1] < nums[i]:
                    kArr.pop()
                    kArr.append(nums[i])
        
        kArr.sort(reverse = True)
        return kArr[-1]