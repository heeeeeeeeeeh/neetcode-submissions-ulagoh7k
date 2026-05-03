class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        left, right = 0, 1

        while right < len(prices):
            if prices[left] < prices[right]:
                maxP = max(maxP, prices[right]-prices[left])
            else:
                left = right
            right += 1
        return maxP