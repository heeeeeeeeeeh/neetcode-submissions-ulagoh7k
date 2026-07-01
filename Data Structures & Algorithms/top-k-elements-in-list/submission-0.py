class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        freq = Counter(nums)
        for num, count in freq.items():
            buckets[count].append(num)
        res = []
        for b in buckets[::-1]:
            if len(res) < k:
                res.extend(b[:k-len(res)])
        return  res