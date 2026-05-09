class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxL = 0
        seen = {}

        for r in range(len(s)):
            if s[r] in seen:
                l = max(seen[s[r]] + 1, l)
            seen[s[r]] = r
            maxL = max(r-l+1, maxL)
        return maxL