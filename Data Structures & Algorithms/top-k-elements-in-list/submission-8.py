class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        buckets = [[] for _ in range(len(nums)+1)]

        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        for num, count in freq.items():
            buckets[count].append(num)
        
        for b in buckets[::-1]:
            res.extend(b[:k-len(res)])
            if len(res) >= k:
                return res