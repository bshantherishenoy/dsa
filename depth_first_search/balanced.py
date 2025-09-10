# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        self.computeDepth(root)
        return self.balanced

    def computeDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        l = self.computeDepth(root.left)
        r = self.computeDepth(root.right)
        if abs(l - r) > 1:
            self.balanced = False
        return 1 + max(l, r)