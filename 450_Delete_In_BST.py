# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getPredecessor(self, root):
        root = root.left
        while root.right:
            root = root.right
        
        return root.val
    
    def getSuccessor(self, root):
        root = root.right
        while root.left:
            root = root.left
        
        return root.val
            
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if not (root.left or root.right):
                return None
            if root.right:
                root.val = self.getSuccessor(root)
                root.right = self.deleteNode(root.right, root.val)
            else:
                root.val = self.getPredecessor(root)
                root.left = self.deleteNode(root.left, root.val)
        
        return root
        
        