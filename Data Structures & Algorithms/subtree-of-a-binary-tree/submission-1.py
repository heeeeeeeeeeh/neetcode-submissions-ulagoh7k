# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        rootS = self.serialize(root)
        subS = self.serialize(subRoot)
        combined = subS + "|" + rootS
        z = self.z_function(combined)
        for i in range(len(subS)+ 1, len(combined)):
            if z[i] == len(subS):
                return True
        return False
    
    def serialize(self, root):
        if not root:
            return "#"
        return (str(root.val) + 
                self.serialize(root.left) +
                self.serialize(root.right))
    
    def z_function(self, s):
        l = r = 0
        z = [0]*len(s)
        for i in range(1, len(s)):
            if i <= r:
                z[i] = min(z[i-l], r-i+1)
            while i + z[i] < len(s) and s[z[i]] == s[i + z[i]]:
                z[i] += 1
            if i + z[i] - 1 > r:
                l, r = i, i + z[i]-1
        return z
