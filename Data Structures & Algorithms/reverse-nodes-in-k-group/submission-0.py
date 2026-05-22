# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = prevGroup = ListNode(0, head)

        while True:
            kth = getKth(prevGroup, k)
            if not kth:
                break
            
            nextGroup = kth.next
            prev, cur = kth.next, prevGroup.next
            while cur != nextGroup:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            
            tmp = prevGroup.next
            prevGroup.next = kth
            prevGroup = tmp
        return dummy.next
def getKth(cur, k):
    while cur and k > 0:
        cur = cur.next
        k -= 1
    return cur