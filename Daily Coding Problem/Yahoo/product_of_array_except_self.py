# https://leetcode.com/problems/product-of-array-except-self/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        L = [1]*len(nums)
        
        for i in range(1,len(nums)):
            L[i] = L[i-1]*nums[i-1]
        
        print(L)
        post = 1
        for i in range(len(nums)-1,-1,-1):
            L[i] = post  * L[i]
            post = post * nums[i]
        
        return L
    
    
        
#         L = [1]*len(nums)
#         R = [1]*len(nums)
        
#         for i in range(1,len(nums)):
#             L[i] = L[i-1]*nums[i-1]
            
#         for i in range(len(nums)-2,-1,-1):
#             R[i] = R[i+1]*nums[i+1]
        
#         for i in range(len(nums)):
#             nums[i] = L[i]*R[i]
            
#         return nums
        
        
        
        
        
        
#         With division operator

#         count_zero = 0
#         multi = 1
#         for i in nums:
#             if i == 0:
#                 count_zero += 1
#             else:
#                 multi *= i
        
#         if count_zero > 1:
#             return [0]*len(nums)
#         elif count_zero == 1:
#             for i in range(len(nums)):
#                 if nums[i] == 0:
#                     nums[i] = multi
#                 else:
#                     nums[i] = 0        
#         else:
#             for i in range(len(nums)):
#                 nums[i] = multi//nums[i]
            
            
#         return nums