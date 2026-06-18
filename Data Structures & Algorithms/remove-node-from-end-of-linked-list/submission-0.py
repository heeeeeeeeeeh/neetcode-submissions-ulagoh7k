# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        while n > 0:
            n -= 1
            slow = slow.next
        dummy = cur = ListNode(0, head)
        while slow:
            slow = slow.next
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next