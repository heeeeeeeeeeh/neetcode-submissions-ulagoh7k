class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        buckets = [[] for i in range(len(nums)+1)]

        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        for num, count in freq.items():
            buckets[count].append(num)
        
        for i in range(len(buckets)-1,-1,-1):
            for num in buckets[i]:
                res.append(num)
                if len(res) >= k:
                    return res