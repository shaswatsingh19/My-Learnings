# https://leetcode.com/problems/koko-eating-bananas/
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        low = 1
        # low  = 1 as it could not be lower than that but also l!= min(piles) as there will be a possible if low < min(piles)
        high = max(piles)
        ans = high
        while low<=high:
            mid = low + (high-low)//2
            cnt = 0
            for i in piles:
                cnt += math.ceil(i/mid)
                
            if cnt<= h:
                ans = mid
                high = mid -1
            else:
                low = mid + 1
            
        return ans
            