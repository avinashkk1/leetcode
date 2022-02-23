# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        
        def getHeightOfBinaryTree(root):
            if root is None:
                return -1
            
            nonlocal diameter
            
            leftTreeHeight = getHeightOfBinaryTree(root.left)
            rightTreeHeight = getHeightOfBinaryTree(root.right)
            
            diameter = max(diameter, 2 + leftTreeHeight + rightTreeHeight)
            return 1 + max(leftTreeHeight, rightTreeHeight)
        
        getHeightOfBinaryTree(root)
        return diameter
            
            
            
        