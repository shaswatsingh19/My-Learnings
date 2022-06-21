# https://leetcode.com/problems/merge-sorted-array/
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        i = m-1
        j = n-1
        
        for k in range(m+n-1,-1,-1):
            if j<0:
                return
            if i>=0 and nums1[i]>nums2[j]:
                nums1[k] = nums1[i]
                i-=1
            else:
                nums1[k] = nums2[j]
                j-=1
                
        
#         i = m-1 # starting pointer of nums1
#         j = m+n-1 # ending pointer of nums1
#         k = n-1 # ending pointer of nums2
        
#         while k>-1 and j>-1 and i>-1:
#             if nums1[i]<=nums2[k]:
#                 nums1[j] = nums2[k]
#                 k-=1
#             else:
#                 nums1[j] = nums1[i]
#                 nums1[i] = 0
#                 i-=1
#             j-=1
                
#         while k>-1:
#             nums1[j]= nums2[k]
#             k-=1
#             j-=1