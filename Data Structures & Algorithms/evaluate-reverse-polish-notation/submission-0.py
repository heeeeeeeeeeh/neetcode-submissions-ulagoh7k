class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                b = stack.pop()
                stack.append(stack.pop() - b)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                b = stack.pop()
                stack.append(int(stack.pop() / b))
            else:
                stack.append(int(c))
        return stack[-1]