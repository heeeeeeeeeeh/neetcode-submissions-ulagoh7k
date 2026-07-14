class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        def gen(openN, closeN):
            if openN == closeN == n:
                print("".join(stack))
                res.append("".join(stack))
                return
            if openN < n:
                print("".join(stack))
                stack.append('(')
                gen(openN + 1, closeN)
                stack.pop()
                print("".join(stack))
            if closeN < openN:
                print("".join(stack))
                stack.append(')')
                gen(openN, closeN + 1)
                stack.pop()
                print("".join(stack))
        gen(0,0)
        return res