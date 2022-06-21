class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        fi_max = max(nums)
        nums.remove(fi_max)
        se_max = max(nums)
        nums.remove(se_max)
        fi_min = min(nums)
        nums.remove(fi_min)
        se_min = min(nums)
        print(fi_max, se_max,fi_min, se_min)
        ans =   (fi_max * se_max) - (fi_min* se_min)
        print(ans)
        return ans