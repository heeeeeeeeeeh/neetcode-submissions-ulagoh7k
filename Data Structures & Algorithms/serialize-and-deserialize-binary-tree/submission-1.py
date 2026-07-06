# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "#"
        return (str(root.val) + "."
                + self.serialize(root.left) + "."
                + self.serialize(root.right))
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(".")
        i = 0
        def dfs():
            nonlocal i
            if vals[i] == "#":
                i += 1
                return None
            root = TreeNode(vals[i])
            i += 1
            root.left = dfs()
            root.right = dfs()
            return root
        return dfs()