class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        countT = defaultdict(int)
        countS = defaultdict(int)
        res, resLen = [-1,-1], float("inf")

        for c in t:
            countT[c] += 1

        need, have = len(countT), 0
        l = 0
        for r in range(len(s)):
            c = s[r]
            countS[c] += 1
            if c in countT and countS[c] == countT[c]:
                have += 1
            
            while have == need:
                if r-l+1 < resLen:
                    resLen = r-l+1
                    res = [l, r]
                c = s[l]
                countS[c] -= 1
                if c in countT and countS[c] < countT[c]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float("inf") else ""