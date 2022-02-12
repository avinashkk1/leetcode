from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        levelOrderList = []
        levelItems = []
        queue = deque()
        queue.append(root)
        queue.append(None)
        
        while queue:
            curr = queue.popleft()
            
            if curr:
                levelItems.append(curr.val)
                
                if curr.left:
                    queue.append(curr.left)                    
                if curr.right:
                    queue.append(curr.right)                    
            else:
                if levelItems:
                    levelOrderList.append(levelItems)
                    levelItems = []
                queue.append(None)
                
        
            if len(queue) == 1 and queue[0] is None:
                if levelItems:
                    levelOrderList.append(levelItems)
                break
        
        
        return levelOrderList
                
        
        
        
        
        
    def levelOrder1(self, root: Optional[TreeNode]) -> List[List[int]]:
        levelOrderList = []
        
        def levelOrderRec(node, level):
            if node is None:
                return
            
            if len(levelOrderList) == level:
                levelOrderList.append([])
            
            levelOrderList[level].append(node.val)
            
            if node.left:
                levelOrderRec(node.left, level + 1)
            if node.right:
                levelOrderRec(node.right, level + 1)
                
                
        levelOrderRec(root, 0)
        return levelOrderList
        