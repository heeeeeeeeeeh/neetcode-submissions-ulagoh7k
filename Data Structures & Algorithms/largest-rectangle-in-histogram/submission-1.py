class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxA = 0
        stack = []
        for i, h in enumerate(heights):
            starti = i
            while stack and stack[-1][1] > h:
                stackI, stackH = stack.pop()
                starti = stackI
                maxA = max(maxA, stackH * (i-stackI))
            stack.append((starti, h))
        while stack:
            stackI, stackH = stack.pop()
            maxA = max(maxA, stackH * (len(heights) - stackI))
        return maxA