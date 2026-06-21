class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, len(prices)-1
        maxP = 0
        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            else:
                maxP = max(maxP, prices[r]-prices[l])
        return maxP