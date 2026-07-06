class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxF = maxL = l = 0
        count = defaultdict(int)
        for r in range(len(s)):
            count[s[r]] += 1
            maxF = max(maxF, count[s[r]])

            if r-l+1-maxF > k:
                count[s[l]] -= 1
                l += 1
            maxL = max(maxL, r-l+1)
        return maxL