class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxA = 0

        for i,h in enumerate(heights):
            startI = i
            while stack and h < stack[-1][1]:
                stackI, stackH = stack.pop()
                maxA = max(maxA, (i-stackI)*stackH)
                startI = stackI
            stack.append((startI,h))
        
        while stack:
            i,h = stack.pop()
            maxA = max(maxA, (len(heights)-i)*h)
        return maxA