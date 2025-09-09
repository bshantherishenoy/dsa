# https://leetcode.com/problems/symmetric-tree/description/?envType=problem-list-v2&envId=depth-first-search
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return root and self.check(root.left,root.right)



    def check(self,p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        if p!=None and q==None or p==None and q!=None:
            return False
        return p.val == q.val and self.check(p.left,q.right) and self.check(p.right,q.left)