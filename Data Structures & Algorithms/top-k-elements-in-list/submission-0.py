class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums)+ 1)]
        freqMap = defaultdict(int)
        res = []

        for num in nums:
            freqMap[num] += 1
        
        for key,value in freqMap.items():
            buckets[value].append(key)
        

        for b in buckets[::-1]:
            if len(res) >= k:
                break
            res.extend(b[:k-len(res)])
        return res