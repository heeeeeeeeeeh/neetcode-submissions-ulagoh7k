class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        heapq.heapify(nums)
        self.k = k
        while len(nums) > k:
            heapq.heappop(nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        heapq.heappop(self.nums) if len(self.nums) > self.k else None
        return self.nums[0]