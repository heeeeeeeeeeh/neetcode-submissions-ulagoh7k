class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums)+ 1)]
        res = []
        freq = Counter(nums)
        for num, count in freq.items():
            bucket[count].append(num)
        
        for b in bucket[::-1]:
            if len(res) < k:
                res.extend(b[:k-len(res)])
        return res