class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        res = []

        for num in nums:
            count[num] += 1
        freq = [[] for _ in range(len(nums) + 1)]

        for num,c in count.items():
            freq[c].append(num)
        
        for b in freq[::-1]:
            if len(res) < k:
                res.extend(b[:k-len(res)])
        return res