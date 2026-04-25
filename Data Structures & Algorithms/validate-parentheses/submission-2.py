class Solution:
    def isValid(self, s: str) -> bool:
        close = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = []

        for c in s:
            if c in close.keys():
                if len(stack) == 0 or stack[-1] != close[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        if not len(stack) == 0:
            return False
        return True