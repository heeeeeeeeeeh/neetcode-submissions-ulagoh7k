# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0
            nonlocal res
            leftMax = max(dfs(root.left), 0)
            rightMax = max(dfs(root.right), 0)
            res = max(res, root.val + leftMax + rightMax)
            return root.val + max(leftMax, rightMax)
        res = root.val
        dfs(root)
        return res