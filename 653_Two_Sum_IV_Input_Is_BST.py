# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if root is None:
            return False
        
        leftStack = []
        rightStack = []
        
        def addLeftNodes(node):
            while node:
                leftStack.append(node)
                node = node.left
        
        def addRightNodes(node):
            while node:
                rightStack.append(node)
                node = node.right
        
        addLeftNodes(root)
        addRightNodes(root)
        
        while leftStack[-1] != rightStack[-1]:
            nodeSum = leftStack[-1].val + rightStack[-1].val
            if nodeSum == k:
                return True
            
            if nodeSum < k:
                currNode = leftStack.pop()
                
                if currNode.right:
                    addLeftNodes(leftStack, currNode.right)
            else:
                currNode = rightStack.pop()
                
                if currNode.left:
                    addRightNodes(rightStack, currNode.left)
        
        return False
    
            
            
        
        
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        BSTSet = set()
        
        def dfs(root):
            if root is None:
                return False
            
            if k - root.val in BSTSet:
                return True
            
            BSTSet.add(root.val)
            
            return dfs(root.left) or dfs(root.right)
        
        return dfs(root)
        
        
            