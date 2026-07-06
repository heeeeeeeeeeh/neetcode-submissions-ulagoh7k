class Solution:
    def isValid(self, s: str) -> bool:
        close = {
            ']': '[',
            '}': '{',
            ')': '('
        }
        stack = []
        for c in s:
            if c in close:
                if not stack or stack[-1] != close[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return not stack