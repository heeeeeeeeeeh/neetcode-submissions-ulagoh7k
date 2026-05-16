class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        res, resLen = [-1,-1], float("inf")

        tCount = defaultdict(int)
        sCount = defaultdict(int)
        for c in t:
            tCount[c] += 1
        
        have, need = 0, len(tCount)
        l = 0
        for r in range(len(s)):
            c = s[r]
            sCount[c] += 1

            if c in tCount and sCount[c] == tCount[c]:
                have += 1
            
            while have == need:
                if (r-l+1) < resLen:
                    res = [l, r]
                    resLen = r-l+1

                sCount[s[l]] -= 1
                if s[l] in tCount and sCount[s[l]] < tCount[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float("inf") else ""