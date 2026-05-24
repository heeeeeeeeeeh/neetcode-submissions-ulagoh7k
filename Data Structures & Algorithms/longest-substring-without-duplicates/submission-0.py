class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        maxL = 0
        
        l = 0
        for r in range(len(s)):
            if s[r] in seen:
                l = max(seen[s[r]] + 1, l)
            seen[s[r]] = r

            maxL = max(maxL, r-l+1)
        return maxL