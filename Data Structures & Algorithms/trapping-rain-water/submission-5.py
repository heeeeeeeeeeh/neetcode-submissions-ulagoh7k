class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = height[0]
        maxRight = height[-1]
        res = 0
        left, right = 0, len(height)-1
        while left < right:
            if height[left] < height[right]:
                left += 1
                maxLeft = max(height[left],maxLeft)
                res += maxLeft - height[left]
            else:
                right -= 1
                maxRight = max(height[right],maxRight)
                res += maxRight - height[right]
        return res