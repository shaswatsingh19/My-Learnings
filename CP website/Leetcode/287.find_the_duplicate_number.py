# https://leetcode.com/problems/find-the-duplicate-number/
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast :
                break
        slow = nums[0]    
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            
        return slow
            
        
        
        
        
#         count = collections.Counter(nums)
        
    
#         for k,v in count.items():
#             if v>1:
#                 return k
        