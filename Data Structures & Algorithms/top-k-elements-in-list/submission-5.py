class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums))]
        res = []
        
        c = Counter(nums)

        for value, key in c.items():
            buckets[key-1].append(value)

        for i in range(len(buckets)-1,-1,-1):
            for j in buckets[i]:
                res.append(j)
                if len(res) == k:
                    return res