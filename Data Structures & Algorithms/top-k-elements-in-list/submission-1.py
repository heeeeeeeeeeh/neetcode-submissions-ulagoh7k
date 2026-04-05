from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freq = [[] for i in range(len(nums) + 1)]
        res = []

        for v,f in count.items():
            freq[f].append(v)

        for i in range(len(freq)-1,0,-1):
            for v in freq[i]:
                res.append(v)
                if len(res) == k:
                    return res