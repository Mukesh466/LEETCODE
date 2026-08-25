# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        sums, level = [], [root]
        while level:
            sums.append(sum(n.val for n in level))
            level = [c for n in level for c in (n.left, n.right) if c]
        return sums.index(max(sums)) + 1