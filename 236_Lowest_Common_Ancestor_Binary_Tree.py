# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def LCARec(root, p, q):
            if root is None:
                return None
            
            if root == p or root == q:
                return root
            
            leftTree = LCARec(root.left, p, q)
            rightTree = LCARec(root.right, p, q)
            
            if leftTree and rightTree:
                return root
            
            return leftTree if leftTree else rightTree
            
        
        return LCARec(root, p, q)
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root]
        parentDict = {root:None}
        
        while p not in parentDict or q not in parentDict:
            curr = stack.pop()
            
            if curr.left:
                parentDict[curr.left] = curr
                stack.append(curr.left)
            
            if curr.right:
                parentDict[curr.right] = curr
                stack.append(curr.right)
        
        ancestorsOfP = set()
        while p:
            ancestorsOfP.add(p)
            p = parentDict[p]
        
        while q not in ancestorsOfP:
            q = parentDict[q]
        
        return q
            
            
            
            
        