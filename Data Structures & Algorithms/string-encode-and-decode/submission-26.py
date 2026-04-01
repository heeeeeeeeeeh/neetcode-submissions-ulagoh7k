class Solution:


    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        end = 0
        start = 0

        while True:
            end = s.find("#",start)
            if end == -1:
                break
            length = int(s[start:end])
            end = end + 1
            res.append(s[end:end + length])
            start = end + length

        return res