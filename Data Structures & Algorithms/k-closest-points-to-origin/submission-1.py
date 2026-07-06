class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x,y in points:
            heapq.heappush_max(heap, (x**2 + y**2, x, y))
            if len(heap) > k:
                heapq.heappop_max(heap)
        res = []
        while k > 0:
            k -= 1
            res.append(heapq.heappop(heap)[1:])
        return res