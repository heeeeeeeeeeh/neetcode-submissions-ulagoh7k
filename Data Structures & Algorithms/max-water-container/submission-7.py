class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        maxA = 0

        while left < right:
            if heights[left] < heights[right]:
                area = heights[left] * (right-left)
                maxA = max(maxA,area)
                left += 1
            else:
                area = heights[right] * (right-left)
                maxA = max(maxA,area)
                right -= 1
        return maxA