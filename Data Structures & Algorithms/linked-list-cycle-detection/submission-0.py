# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        cur = head
        seen.add(cur)

        while cur:
            if cur.next in seen:
                return True
            cur = cur.next
            seen.add(cur)
        return False