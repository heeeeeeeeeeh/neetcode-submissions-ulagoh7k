class Solution:
    def isValid(self, s: str) -> bool:
        closing = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []
        for c in s:
            if c in closing:
                if not stack or stack[-1] != closing[c]:
                    return False
                stack.pop()
            elif c in closing.values():
                stack.append(c)
        return False if stack else True