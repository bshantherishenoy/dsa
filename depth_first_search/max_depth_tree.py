import unittest
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.arr = []
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        count = 0
        total = 0
        self.inorder(root,total,count)
        print(f"{count}---{total}")
        return total
        
    def inorder(self,root:Optional[TreeNode],total,count) -> int:
        if not root:
            return total
        count+=1
        total = max(total,count)
        print(f"{root.val}____{count}____{total}")
        self.inorder(root.left,total,count)
        count = 1
        self.inorder(root.right,total,count)
    
        
            
            
        
        
class Test_inorder(unittest.TestCase):
    def test_example1(self):
        self.sol = Solution()
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        self.assertEqual(self.sol.maxDepth(root),3)
        
    
       
        
if __name__ == '__main__':
    unittest.main()

