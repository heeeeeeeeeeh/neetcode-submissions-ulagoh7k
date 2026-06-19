# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def serialize(self, root):
        if not root:
            return "$#"
        return ("$" + str(root.val) +
                self.serialize(root.left) +
                self.serialize(root.right))
    
    def z_function(self, s):
        l=r=0
        z = [0]*len(s)
        for i in range(1,len(s)):
            if i <= r:
                z[i] = min(z[i-l], r-l+1)
            while z[i] + i < len(s) and s[z[i]] == s[i + z[i]]:
                z[i] += 1
            if i + z[i] - 1 > r:
                l, r = i, i + z[i] - 1
        return z
    def isSubtree(self, root, subRoot):
        subRootS = self.serialize(subRoot)
        combined = subRootS + "|" + self.serialize(root)
        z = self.z_function(combined)
        for i in range(len(subRootS) + 1, len(combined)):
            if z[i] == len(subRootS):
                return True
        return False
    