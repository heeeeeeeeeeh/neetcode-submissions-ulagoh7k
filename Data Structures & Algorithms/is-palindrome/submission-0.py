class Solution:
    #Understand: check if string is a palidrome
    #Plan:
    #Init left to first elem and right pointer to last elem
    # loop while left pointer not greater then right pointer
        # skip nonlphanumeric characters 
        # if left pointer and right pointer are not equal 
            # return false
    # return True
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True