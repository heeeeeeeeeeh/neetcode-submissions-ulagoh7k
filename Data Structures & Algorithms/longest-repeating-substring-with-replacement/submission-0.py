class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxf = 0
        l = 0
        maxL = 0
        count = defaultdict(int)
        for r in range(len(s)):
            count[s[r]] += 1
            maxf = max(maxf, count[s[r]])
            while (r-l+1)-maxf > k:
                count[s[l]] -= 1
                l += 1
            maxL = max(maxL, (r-l) + 1)
        return maxL
