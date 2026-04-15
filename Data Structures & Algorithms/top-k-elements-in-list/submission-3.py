from collections import Counter, defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = Counter(nums)
        buckets = [[] for i in range(len(nums))]

        for value,key in freqMap.items():
            print(key,value)
            buckets[key-1].append(value)
        
        res = []
        print(buckets)
        for i in range(len(buckets)-1,-1,-1):
            print(buckets[i])
            for num in buckets[i]:
                if len(res) < k:
                    res.append(num)
                else:
                    break
            if len(res) == k:
                break
        return res