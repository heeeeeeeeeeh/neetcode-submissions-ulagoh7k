class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and stack[-1][1] < temperatures[i]:
                stackI, stackT = stack.pop()
                res[stackI] = i - stackI
            stack.append((i,temperatures[i]))
        return res