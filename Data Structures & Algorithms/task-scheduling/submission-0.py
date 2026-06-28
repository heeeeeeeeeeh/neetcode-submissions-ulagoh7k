class Heap:
    def __init__(self, nums):
        self.buildHeap(nums)
    
    def buildHeap(self, nums):
        self.nums = nums
        for i in range(len(nums)-1, -1,-1):
            self.heapifyDown(i)
    
    def heapifyDown(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        m = i
        
        if left < len(self.nums) and self.nums[left] < self.nums[m]:
            m = left
        if right < len(self.nums) and self.nums[right] < self.nums[m]:
            m = right
        
        if i != m:
            self.nums[i], self.nums[m] = self.nums[m], self.nums[i]
            self.heapifyDown(m)
    
    def heapifyUp(self, i):
        parent = (i-1)//2
        if i > 0 and self.nums[i] < self.nums[parent]:
            self.nums[i], self.nums[parent] = self.nums[parent], self.nums[i]
            self.heapifyUp(parent)
    
    def insert(self, val):
        self.nums.append(val)
        self.heapifyUp(len(self.nums)-1)
    
    def pop(self):
        if len(self) == 1:
            return self.nums.pop()
        val, self.nums[0] = self.nums[0], self.nums.pop()
        self.heapifyDown(0)
        return val
    
    def getMin(self):
        return self.nums[0]
    
    def __len__(self):
        return len(self.nums)

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        count = [-cnt for cnt in count.values()]
        heap = Heap(count)
        q = deque()
        time = 0

        while q or heap:
            time += 1
            if not count:
                time = q[0][1]
            else:
                cnt = 1 + heap.pop()
                if cnt:
                    q.append((cnt, time + n))
            if q and q[0][1] == time:
                heap.insert(q.popleft()[0])
        return time