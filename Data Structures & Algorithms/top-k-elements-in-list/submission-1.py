class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        res = []
        freq = Counter(nums)
        for num, count in freq.items():
            bucket[count].append(num)

        for arr in bucket[::-1]:
            if len(res) >= k:
                break
            res.extend(arr[:k-len(res)])
        return res