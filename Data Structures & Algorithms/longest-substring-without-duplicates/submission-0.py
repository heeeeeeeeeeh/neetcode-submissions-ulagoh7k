class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        win = {}
        l = 0
        maxL = 0
        for r in range(len(s)):
            if s[r] in win:
                l = max(win[s[r]] + 1, l)
            win[s[r]] = r
            maxL = max(maxL, r-l+1)
        return maxL