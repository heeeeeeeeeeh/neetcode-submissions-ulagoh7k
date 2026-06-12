# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, maxN):
            nonlocal res;
            if not root:
                return
            if maxN <= root.val:
                res += 1
            maxN = max(maxN, root.val)
            dfs(root.left, maxN)
            dfs(root.right, maxN)
        res = 0
        dfs(root,float("-inf"))
        return res