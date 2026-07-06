class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxF = max(count.values())
        maxC = len(list(filter(lambda x : x == maxF, count.values())))
        
        time = (maxF-1)*(n+1)+maxC
        return max(len(tasks), time)