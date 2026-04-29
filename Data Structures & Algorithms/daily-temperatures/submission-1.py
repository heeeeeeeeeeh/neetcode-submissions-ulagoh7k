# Understand: for each day find the nearest 
# day in the future that is warmer
# Plan:
# init a stack for previous days
# init array to zeros where index is the current day
# and value is index of the future day
# loop through each day
    # while the top of the stack is colder than current day
        # set value in array of the day in top of stack 
        # to the difference of teh days
    # append index of current day and temp to stack

# return resulting array
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []

        for i,temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                stackI,stackTemp = stack.pop()
                res[stackI] = i - stackI
            stack.append((i,temp))
        return res
