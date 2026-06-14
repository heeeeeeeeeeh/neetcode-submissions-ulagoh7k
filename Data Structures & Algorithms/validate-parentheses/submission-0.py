class Solution:
    def isValid(self, s: str) -> bool:
        close = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        stack = []
        for c in s:
            if c in close:
                if not stack or close[c] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return len(stack) == 0