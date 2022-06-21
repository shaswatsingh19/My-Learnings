# https://leetcode.com/problems/sort-even-and-odd-indices-independently/
class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        
        even = []
        odd = []
        for i in range(len(nums)):
            if i%2==0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
                
                
        even.sort()
        odd.sort(reverse=True)
        
        print(even)
        print(odd)
        
        j = 0
        for i in range(0,len(nums),2):
            nums[i] = even[j]
            j+=1
            
        j = 0
        for i in range(1,len(nums),2):
            nums[i] = odd[j]
            j+=1
        return nums
            