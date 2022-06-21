# https://leetcode.com/problems/valid-mountain-array/submissions/
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        
        if n<3 or arr[0]>=arr[1] or arr[-1] >=arr[-2]:
            return False
        
        i=1
        while (i<n):
            if arr[i]>arr[i-1] and arr[i]<arr[i+1]:
                i+=1
                continue
            else:
                break
                
        
        while(i<n-1):
            if arr[i]>arr[i+1]:
                i+=1  
            else:
                return False
        return True