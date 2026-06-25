class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        buy = prices[0]
        for price in prices:
            if price < buy:
                buy = price
            if price > buy:
                profit = price - buy
                if profit > maxprofit:
                    maxprofit = profit
        return maxprofit