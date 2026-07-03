# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        i = j = 0
        n = len(preorder)
        head = cur = TreeNode()
        while i < n and j < n:
            cur.right = TreeNode(preorder[i], right = cur.right)
            cur = cur.right
            i += 1
            while i < n and cur.val != inorder[j]:
                cur.left = TreeNode(preorder[i], right = cur)
                cur = cur.left
                i += 1
            j += 1
            while j < n and cur.right and cur.right.val == inorder[j]:
                cur.right, cur = None, cur.right
                j += 1
        return head.right