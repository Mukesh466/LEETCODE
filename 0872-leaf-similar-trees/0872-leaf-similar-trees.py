# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def getroot(root):
            if root is None:
                return []
            leaf=getroot(root.left) + getroot(root.right)
            return leaf or [root.val]
        return getroot(root1) == getroot(root2)        