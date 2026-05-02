class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i, height in enumerate(heights):
            startI = i
            while stack and stack[-1][1] > height:
                stackI, stackH = stack.pop()
                area = stackH * (i-stackI)
                maxArea = max(area,maxArea)
                startI = stackI
            stack.append((startI,height))
        
        while stack:
            index, height = stack.pop()
            area = height * (len(heights)-index)
            maxArea = max(maxArea, area)
        return maxArea
