# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prevGroup = dummy = ListNode(0,head)

        while True:
            kth = self.getKthNode(prevGroup, k)
            if not kth:
                break

            prev = nextGroup = kth.next
            cur = prevGroup.next
            while cur != nextGroup:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp

            prevGroup.next, prevGroup = kth,prevGroup.next
        return dummy.next
    
    def getKthNode(self, node, k):
        while node and k > 0:
            k -= 1
            node = node.next
        return node