# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = prevGroup = ListNode(0, head)

        while True:
            kth = findKthNode(prevGroup, k)
            if not kth:
                break
            
            nextGroup, prev = kth.next, kth.next
            cur = prevGroup.next
            while cur != nextGroup:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            
            tmp = prevGroup.next
            prevGroup.next = kth
            prevGroup = tmp
        return dummy.next
def findKthNode(node, k):
    for _ in range(k):
        if not node:
            break
        node = node.next
    return node
