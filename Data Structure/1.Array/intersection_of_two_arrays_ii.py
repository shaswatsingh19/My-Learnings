# https://leetcode.com/problems/intersection-of-two-arrays-ii/
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        i = 0
        while(i<len(nums1)):
            if nums1[i] in nums2:
                nums2.remove(nums1[i])
                i+=1
            else:
                nums1.pop(i)
                
        return nums1
                
#         res = []
#         for i in nums1:
#             if i in nums2:
#                 res.append(i)
#                 nums2.remove(i)
        
#         return res

# --------------------------------------------------------------------

#         nums1.sort()
#         nums2.sort()
#         i=0
#         j=0
        
#         while(i<len(nums1) and j<len(nums2)):
#             if nums1[i] == nums2[j]:
#                 i+=1
#                 j+=1
                
#             elif nums1[i]<nums2[j]:
#                 nums1.pop(i)
#             else:
#                 j+=1
                
#         return nums1[:i]

# -------------------------------------------------------------------------
        
#         a = []
        
#         nums1.sort()
#         nums2.sort()
        
#         i = 0
#         j = 0
        
#         while(i<len(nums1) and j<len(nums2)):
            
#             if nums1[i] == nums2[j]:
#                 a.append(nums1[i])
#                 i+=1
#                 j+=1
                
#             elif nums1[i]<nums2[j]:
#                 i+=1
#             else:
#                 j+=1
                
#         return a