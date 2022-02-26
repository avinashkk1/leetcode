# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        currNode = root
        stack = []
        inOrderList = []
        
        while currNode or stack:
            while currNode:
                stack.append(currNode)
                currNode = currNode.left
            
            currNode = stack.pop()
            inOrderList.append(currNode.val)
            currNode = currNode.right
        
        return inOrderList
            
        