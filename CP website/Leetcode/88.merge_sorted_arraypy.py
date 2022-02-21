# https://leetcode.com/problems/merge-sorted-array/
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        if m==0 and n!=0:
            nums1 = nums2
      
        i=0
        j = m
        while(i<n):
            nums1[j] = nums2[i]
            i+=1
            j+=1
            
        i = 0
        j = m
        
        while(i<(m+n)):
            
            if (i<j):
                if(nums1[i]<=nums1[j]):
                    i+=1
                else:
                    nums1[i],nums1[j] = nums1[j],nums1[i] 
                    i+=1
            else:
                if(nums1[i]>=nums1[j]):
                    i+=1
                else:
                    nums1[i],nums1[j] = nums1[j],nums1[i] 
                    j+=1
                