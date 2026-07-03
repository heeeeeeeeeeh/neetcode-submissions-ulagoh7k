# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cur = root
        while cur:
            if cur.left:
                prev = cur.left
                while prev.right and cur != prev.right:
                    prev = prev.right
                if prev.right:
                    k -= 1
                    if k == 0:
                        return cur.val
                    cur = cur.right
                else:
                    prev.right = cur
                    cur = cur.left
            else:
                k -= 1
                if k == 0:
                    return cur.val
                cur = cur.right
        return -1
