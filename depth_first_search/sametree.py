import unittest
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p==None and q==None:
            return True
        if p!=None and q==None or p==None and q!=None:
            return False
        return p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right) 
        
            
            
        
        
class Test_inorder(unittest.TestCase):

            
    def test_example1(self):
        self.sol = Solution()
        root1 = TreeNode(1)
        root1.left = TreeNode(2)
        root1.right = TreeNode(3)
        root2 = TreeNode(1)
        root2.left = TreeNode(2)
        root2.right = TreeNode(3)
        self.assertEqual(self.sol.isSameTree(root1,root2),True)
        
    def test_example2(self):
        self.sol = Solution()
        root1 = TreeNode(1)
        root1.left = TreeNode(2)
        root2 = TreeNode(1)
        root2.right = TreeNode(2)
        self.assertEqual(self.sol.isSameTree(root1,root2),False)
       
        
if __name__ == '__main__':
    unittest.main()

