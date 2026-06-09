# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prevG = dummy = ListNode(0, head)

        while True:
            kth = self.getKthNode(prevG, k)
            if not kth:
                break
            nextGroup = kth.next
            prev, cur = nextGroup, prevG.next
            while cur != nextGroup:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            
            tmp = prevG.next
            prevG.next = kth
            prevG = tmp
        return dummy.next

    def getKthNode(self, node, k):
        while node and k > 0:
            k -= 1
            node = node.next
        return node