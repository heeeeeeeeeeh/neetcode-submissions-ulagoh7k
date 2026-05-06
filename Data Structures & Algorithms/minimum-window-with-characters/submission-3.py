class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        tCount, sCount = defaultdict(int), defaultdict(int) 
        for c in t:
            tCount[c] += 1
        
        res, resLen = [-1,-1], float("inf")
        l, have, need = 0, 0, len(tCount)
        for r in range(len(s)):
            c = s[r]
            sCount[c] += 1
            if c in tCount and sCount[c] == tCount[c]:
                have += 1
            
            while need == have:
                if (r-l+1) < resLen:
                    resLen = r-l+1
                    res = [l, r]
                sCount[s[l]] -= 1
                if s[l] in tCount and sCount[s[l]] < tCount[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float("inf") else ""
