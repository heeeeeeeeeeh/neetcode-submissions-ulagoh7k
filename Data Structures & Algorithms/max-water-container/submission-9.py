class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        maxA = 0

        while l < r:
            if heights[l] < heights[r]:
                maxA = max(maxA, heights[l] * (r-l))
                l += 1
            else:
                maxA = max(maxA, heights[r] * (r-l))
                r -= 1
        return maxA