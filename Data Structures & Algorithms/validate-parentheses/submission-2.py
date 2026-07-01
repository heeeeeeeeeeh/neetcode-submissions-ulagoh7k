class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close = {
            ']': '[',
            ')': '(',
            '}': '{',
        }
        for c in s:
            if c in close:
                if not stack or stack[-1] != close[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return True if not stack else False