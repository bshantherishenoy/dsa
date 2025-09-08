import unittest
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.arr = []
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.inorder(root)
        return self.arr
        
    def inorder(self,root:Optional[TreeNode]) -> None:
        if not root:
            return 
        
        self.inorder(root.left)
        self.arr.append(root.val)
        self.inorder(root.right)
        
            
            
        
        
class Test_inorder(unittest.TestCase):

            
    def test_example1(self):
        self.sol = Solution()
        root = TreeNode(1)
        root.left = None
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)
        self.assertEqual(self.sol.inorderTraversal(root),[1,3,2])
        
    def test_example2(self):
        self.sol = Solution()
        root = TreeNode(1)
        root.left= TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.left.right.left = TreeNode(6)
        root.left.right.right = TreeNode(7)
        root.right.left = None
        root.right.right = TreeNode(8)
        root.right.right.left = TreeNode(9)
        self.assertEqual(self.sol.inorderTraversal(root),[4,2,6,5,7,1,3,9,8])
       
        
if __name__ == '__main__':
    unittest.main()
