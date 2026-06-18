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
        new = defaultdict(lambda : Node(0))
        new[None] = None

        cur = head
        while cur:
            new[cur].val = cur.val
            new[cur].random = new[cur.random]
            new[cur].next = new[cur.next]
            cur = cur.next
        return new[head]