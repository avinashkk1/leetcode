from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        postOrderList = deque()
        stack = []
        stack.append(root)
        
        while stack:
            currNode = stack.pop()
            postOrderList.appendleft(currNode.val)
            
            if currNode.left:
                stack.append(currNode.left)
            
            if currNode.right:
                stack.append(currNode.right)
        
        return postOrderList
    
       
    def postorderTraversal1(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        postOrderList = []
        
        def postOrder(root):
            if root is None:
                return
            
            if root.left:
                postOrder(root.left)
            
            if root.right:
                postOrder(root.right)
            
            postOrderList.append(root.val)
        
        postOrder(root)
        return postOrderList
        