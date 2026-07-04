class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            heapq.heappush_max(heap, [x**2 + y**2, x, y])
            if len(heap) > k:
                heapq.heappop_max(heap)
        for i in range(len(heap)):
            heap[i].pop(0)
        return heap
        