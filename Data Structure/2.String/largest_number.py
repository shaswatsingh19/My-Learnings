# https://leetcode.com/problems/largest-number/
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        string = []
        for num in nums:
            string.append(str(num))
            
        string.sort(key = functools.cmp_to_key(self.compare))
        ans = ''
        for i in string:
            ans += i 
            
        if ans[0] == '0':
            return '0'
        
        return ans
    
    def compare(self, a, b):
        if a + b > b + a:
            return -1
        return 1
        

#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
                
#                 first = str(nums[i])
#                 second = str(nums[j])
                
#                 ij = int(first+second)
#                 ji = int(second +first)
                
#                 if ij<ji:
#                     nums[i],nums[j] = nums[j],nums[i]
#         ans = ''
#         for i in nums:
#             ans += str(i)
        
#         return str(int(ans))
