class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return "";

        tCount = defaultdict(int)
        for c in t:
            tCount[c] += 1
        
        res, resLen = [-1,-1], float("inf")
        for i in range(len(s)):
            sCount = defaultdict(int)
            for j in range(i,len(s)):
                sCount[s[j]] += 1

                flag = True
                for c in tCount:
                    if sCount[c] < tCount[c]:
                        flag = False
                        break
                if flag and (j-i+1) < resLen:
                    resLen = j-i+1
                    res = [i, j]
        l, r = res
        return s[l:r + 1] if resLen != float("inf") else ""