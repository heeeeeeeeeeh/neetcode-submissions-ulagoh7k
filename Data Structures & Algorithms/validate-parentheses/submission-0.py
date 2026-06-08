class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        stack = []
        for c in s:
            if c in closeToOpen.keys():
                if not stack or stack[-1] != closeToOpen[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return True if not stack else False