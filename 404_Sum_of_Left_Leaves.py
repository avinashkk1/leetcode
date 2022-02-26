# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        leftSum = [0]
        
        def dfs(node, includeFlag):
            if node is None:
                return
            
            if node.left:
                dfs(node.left, True)
            
            if node.right:
                dfs(node.right, False)
        
            if includeFlag and node.left is None and node.right is None:
                leftSum[0] += node.val
            
            
        dfs(root, False)
        return leftSum[0]
            
            
        