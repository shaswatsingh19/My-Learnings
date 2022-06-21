# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/
class Solution:
    def countOdds(self, l: int, h: int) -> int:
        
        return (h-l)//2 if l%2==0 and h%2==0 else (h-l)//2 + 1
        
        