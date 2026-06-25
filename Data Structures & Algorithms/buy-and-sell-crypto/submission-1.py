class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        for i in range(len(prices) - 1):
            profit = max(prices[i+1:]) - prices[i]
            maxprofit = max(profit, maxprofit)
        return maxprofit