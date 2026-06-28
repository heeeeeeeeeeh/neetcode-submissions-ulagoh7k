class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        maxF = max(count.values())
        maxCount = 0
        for i in count.values():
            if i == maxF:
                maxCount += 1
        
        time = (maxF-1) * (n + 1) + maxCount
        return max(len(tasks), time)