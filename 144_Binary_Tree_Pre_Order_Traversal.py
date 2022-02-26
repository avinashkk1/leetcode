# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        preOrderList = []
        stack = [root]
        
        while stack:
            currNode = stack.pop()
            preOrderList.append(currNode.val)
            
            if currNode.right:
                stack.append(currNode.right)
            
            if currNode.left:
                stack.append(currNode.left)
        
        return preOrderList
            
        
        
        
        
    
    def preorderTraversal1(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        preOrderList = []
        
        def preOrder(root):
            if root is None:
                return
            
            preOrderList.append(root.val)
            
            if root.left:
                preOrder(root.left)
                
            if root.right:
                preOrder(root.right)
        
        preOrder(root)
        return preOrderList
        
        
        
        