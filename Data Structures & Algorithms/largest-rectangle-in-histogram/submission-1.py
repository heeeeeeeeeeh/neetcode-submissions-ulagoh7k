class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height:
                stackI, stackH = stack.pop()
                maxArea = max(maxArea, stackH * (i-stackI))
                start = stackI
            stack.append((start,height))
        

        for i, height in stack:
            maxArea = max(maxArea, height * (len(heights)-i))
        return maxArea