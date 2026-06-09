# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return True, 0
            lB, lH = dfs(root.left)
            rB, rH = dfs(root.right)

            return (lB and rB and abs(lH - rH) < 2), 1 + max(lH, rH)
        return dfs(root)[0]