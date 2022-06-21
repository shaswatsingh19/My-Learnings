# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit  = 0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                profit += prices[i] - prices[i-1]
        
        
        
        return profit
    
    
#         peak = prices[0]
#         valley = prices[0]

#         profit = 0
#         n  = len(prices)
#         i=0
#         while i<n-1:
#             while (i<n-1 and prices[i]>=prices[i+1]):
#                 i+=1

#             valley = prices[i]

#             while (i<n-1 and prices[i]<= prices[i+1]):
#                 i+=1

#             peak = prices[i]

#             profit += peak - valley

#         return profit
