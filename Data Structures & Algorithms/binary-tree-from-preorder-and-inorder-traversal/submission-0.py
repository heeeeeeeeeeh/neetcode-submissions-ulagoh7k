# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        head = cur = TreeNode(None)
        i, j, n = 0, 0, len(preorder)
        while i < n and j < n:
            cur.right = TreeNode(preorder[i], right = cur.right)
            cur = cur.right
            i += 1
            while i < n and cur.val != inorder[j]:
                cur.left = TreeNode(preorder[i], right = cur)
                cur = cur.left
                i += 1
            j += 1
            while cur.right and j < n and cur.right.val == inorder[j]:
                cur.right, cur = None, cur.right
                j += 1
        return head.right
