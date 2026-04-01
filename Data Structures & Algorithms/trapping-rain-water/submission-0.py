class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        maxLeft = maxRight = maxSum = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] > maxLeft:
                    maxLeft = height[left]
                else: 
                    maxSum += maxLeft - height[left]
                left += 1
            else:
                if height[right] > maxRight:
                    maxRight = height[right]
                else:
                    maxSum += maxRight - height[right]
                right -= 1
        return maxSum 