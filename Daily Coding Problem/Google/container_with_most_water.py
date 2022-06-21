# https://leetcode.com/problems/container-with-most-water
class Solution:
    def maxArea(self, arr: List[int]) -> int:
        i=0
        j=len(arr)-1
        m=0
        while i<j:
            m = max(m,(j-i)*(min(arr[i],arr[j])))
            if arr[i]<arr[j]:
                i+=1
            else:
                j-=1
        return m
            
        