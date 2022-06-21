# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        i = 0
        j = len(numbers)-1
        while i<j:
            val = numbers[i] + numbers[j]
            if val > target:
                j-=1
            elif val < target:
                i+=1
            else:
                return [i+1,j+1]
        return