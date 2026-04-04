class Solution:
    #Understand: Compute posfix notation from array of strings
    #Plan: create empty stack
    #Loop though each elem in array
        # if current string is "+"
            # pop top two elements
            # add popped elements and append to stack
        # if current string is "-"
            # pop top two elements
            # sub popped elements and append to stack
        # if current string is "*"
            # pop top two elements
            # mul popped elements and append to stack
        # if current string is "/"
            # pop top two elements
            # div popped elements and append to stack
    #return top of stack
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a-b)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(c))
        return stack[0]