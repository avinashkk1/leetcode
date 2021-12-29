# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        prevNode = None
        currNode = root
        leftFlag = False
        while currNode:
            prevNode = currNode
            if currNode.val < val:
                currNode = currNode.right
                leftFlag = False
            else:
                currNode = currNode.left
                leftFlag = True
            
        
        newNode = TreeNode(val)
        if prevNode:
            if leftFlag:
                prevNode.left = newNode
            else:
                prevNode.right = newNode
        else:
            root = newNode
        
        return root
            
        