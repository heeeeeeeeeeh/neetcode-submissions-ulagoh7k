class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxA = 0

        for i, h in enumerate(heights):
            startI = i
            while stack and stack[-1][1] > h:
                stackI, stackH = stack.pop()
                maxA = max(maxA, stackH * (i-stackI))
                startI = stackI
            stack.append((startI, h))
        
        while stack:
            stackI, stackH = stack.pop()
            maxA = max(maxA, stackH * (len(heights) - stackI))
        return maxA
                