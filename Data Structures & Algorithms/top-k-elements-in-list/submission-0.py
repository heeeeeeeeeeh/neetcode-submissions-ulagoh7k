from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket =  [[] for _ in range(len(nums))]
        count = Counter(nums)
        res = []
        maxFreq = 0

        for key,value in count.items():
            maxFreq = max(maxFreq, value-1)
            bucket[value-1].append(key)

        for i in range(maxFreq,-1,-1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    break      
            if len(res) == k:
                break 
        return res