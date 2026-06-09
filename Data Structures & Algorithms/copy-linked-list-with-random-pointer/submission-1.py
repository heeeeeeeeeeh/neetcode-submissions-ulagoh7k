"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old = defaultdict(lambda : Node(0))
        old[None] = None
        cur = head
        newHead = newNode = Node(0)
        while cur:
            newNode.next = old[cur]
            newNode = newNode.next
            newNode.val = cur.val
            newNode.random = old[cur.random]
            cur = cur.next
        return newHead.next