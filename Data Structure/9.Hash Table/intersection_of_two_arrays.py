# https://leetcode.com/problems/intersection-of-two-arrays
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        n1 = set(nums1)
        n2 = set(nums2)
        
        ans = list(n1&n2)
        print(ans)
        return ans

                    