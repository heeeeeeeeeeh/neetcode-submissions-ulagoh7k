class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums)+1)]
        res = []

        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        for num, freq in count.items():
            buckets[freq].append(num)

        for b in buckets[::-1]:
            if len(res) < k:
                res.extend(b[:k-len(res)])
        return res