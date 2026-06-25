class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        l = 0
        r = 0
        for i in range(len(prices)):
            if prices[l] > prices[i]:
                l = i
            else:
                r = i
                profit = prices[r] - prices[l]
                maxprofit = max(profit, maxprofit)
        return maxprofit 