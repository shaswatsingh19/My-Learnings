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

'''
class Solution:
    def topKFrequent(self, nums: List[int], key: int) -> List[int]:
        
        di = {}
        for i in nums:
            if i not in di :
                di[i]  = 1
            else:
                di[i] += 1
                
        arr = []
        i=0
        # min heap logic as we finding the top k
        
        for k,v in di.items():
            if len(arr)<key:
                arr.append([v,k])
            else:
                # checking for top a[0] element is smaller than the current v 
                arr.sort()
                if arr[0][0] < v:
                    # a[0] element frequecy less than current element frequency
                    arr.pop(0)
                    arr.append([v,k])
                    
        arr.sort()
        for i in range(len(arr)):
            arr[i] = arr[i][1]
        
        return arr
'''