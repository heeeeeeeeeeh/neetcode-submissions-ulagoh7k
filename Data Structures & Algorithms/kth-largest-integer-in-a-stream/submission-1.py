class Heap:
    def __init__(self):
        self.nums = []

    def buildHeap(self, nums):
        self.nums = nums
        for i in range(len(nums)-1, -1, -1):
            self.heapifyDown(i)

    def heapifyDown(self, i):
        m = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < len(self.nums) and self.nums[left] < self.nums[m]:
            m = left
        if right < len(self.nums) and self.nums[right] < self.nums[m]:
            m = right
        
        if m != i:
            self.nums[i], self.nums[m] = self.nums[m], self.nums[i]
            self.heapifyDown(m)

    def heapifyUp(self, i):
        if i > 0:
            parent = (i-1)//2
            if self.nums[i] < self.nums[parent]:
                self.nums[i], self.nums[parent] = self.nums[parent], self.nums[i]
                self.heapifyUp(parent)

    def insert(self, num):
        self.nums.append(num)
        self.heapifyUp(len(self.nums)-1)
    
    def pop(self):
        self.nums[0] = self.nums.pop()
        self.heapifyDown(0)
    
    def getMin(self):
        return self.nums[0]

    def __len__(self):
        return len(self.nums)
        
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = Heap()
        self.heap.buildHeap(nums)
        self.k  = k
        while len(self.heap) > k:
            self.heap.pop()


    def add(self, val: int) -> int:
        self.heap.insert(val)
        if len(self.heap) > self.k:
            self.heap.pop()
        return self.heap.getMin()
        
