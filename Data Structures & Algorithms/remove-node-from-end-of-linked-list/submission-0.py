# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = head
        while n > 0:
            n -= 1
            slow = slow.next
        
        res = dummy
        while slow:
            slow = slow.next
            res = res.next
        res.next = res.next.next
        return dummy.next
