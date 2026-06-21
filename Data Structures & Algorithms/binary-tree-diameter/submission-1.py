# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            
            lH = dfs(root.left)
            rH = dfs(root.right)
            res = max(res, lH + rH)
            return 1 + max(lH, rH)
        res = 0
        dfs(root)
        return res