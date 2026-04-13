class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        maxA = 0

        while left < right:
            if heights[right] < heights[left]:
                area = (right-left) * heights[right]
                right -= 1
            else:
                area = (right-left) * heights[left]
                left += 1
            maxA = max(maxA,area)
        return maxA