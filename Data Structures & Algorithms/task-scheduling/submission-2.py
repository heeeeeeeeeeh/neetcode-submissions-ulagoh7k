class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxF = max(freq.values())
        maxCount = len(list(filter(lambda x: x == maxF, freq.values())))
        time = (maxF-1)*(n+1)+maxCount
        return max(time, len(tasks))