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
            else:
                stack.append(c)

        if len(stack) > 0:
            return False
        return True