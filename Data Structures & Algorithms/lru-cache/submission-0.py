class Node:
    def __init__(self, key=0, value=0, nxt=None, prev=None):
        self.key = key
        self.val = value
        self.next = nxt
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        
        self.left, self.right = Node(), Node()
        self.left.next, self.right.prev = self.right, self.left
    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        nxt.prev, prev.next = prev, nxt
    
    def insert(self, node):
        nxt, prev, = self.right, self.right.prev
        nxt.prev = prev.next = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]