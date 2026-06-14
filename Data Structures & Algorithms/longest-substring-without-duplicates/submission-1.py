class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxL = 0
        l = 0
        window = {}
        for r in range(len(s)):
            if s[r] in window:
                l = max(l, window[s[r]] + 1)
            window[s[r]] = r
            maxL = max(maxL, (r-l) + 1)
        return maxL