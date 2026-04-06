class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += s + "ĝ"
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != "ĝ" and j < len(s):
                j += 1
            res.append(s[i:j])
            i = j + 1
        return res
