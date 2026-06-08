class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = {}
        maxL = 0

        for r in range(len(s)):
            if s[r] in seen:
                l = max(l, seen[s[r]] + 1)
            seen[s[r]] = r
            maxL = max(maxL, (r-l)+1)
        return maxL