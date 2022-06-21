# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = 9999999
        profit = 0
        for i in range(len(prices)):
            if prices[i]<mini:
                mini = prices[i]
            diff = prices[i]-mini
            profit = max(profit,diff)
            
        return profit