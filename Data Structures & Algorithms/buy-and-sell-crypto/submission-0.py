class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        maxP = 0

        while sell < len(prices):
            if prices[sell] < prices[buy]:
                buy = sell
            else:
                maxP = max(maxP, prices[sell]-prices[buy])
            sell += 1
        return maxP