class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        maxArea = 0

        while left < right:
            if heights[left] < heights[right]:
                area = (right-left) * heights[left]
                left += 1
            else:
                area = (right-left) * heights[right]
                right -= 1
            maxArea = max(maxArea,area)
        return maxArea