from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            res[tuple(sorted(Counter(s).items()))].append(s)
        return list(res.values())