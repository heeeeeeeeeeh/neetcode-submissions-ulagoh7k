class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '-':
                b = stack.pop()
                stack.append(stack.pop() - b)
            elif token == '*':
                stack.append(stack.pop() * stack.pop())
            elif token == '/':
                b = stack.pop()
                stack.append(int(stack.pop() / b))
            else:
                stack.append(int(token))
        return stack[-1]