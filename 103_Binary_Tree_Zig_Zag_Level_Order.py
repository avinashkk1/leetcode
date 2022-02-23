from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        queue = deque()
        queue.append(root)
        queue.append(None)
        
        leftToRightFlag = True
        nodesInALevel = deque()
        zigZagLevelOrderList = []
        
        while queue:
            curr = queue.popleft()
            
            if curr:
                if leftToRightFlag:
                    nodesInALevel.append(curr.val)
                else:
                    nodesInALevel.appendleft(curr.val)
                
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            else:
                if nodesInALevel:
                    zigZagLevelOrderList.append(nodesInALevel)
                    nodesInALevel = deque()
                queue.append(None)
                leftToRightFlag = (not leftToRightFlag)
            
            if len(queue) == 1 and queue[0] is None:
                if nodesInALevel:
                    zigZagLevelOrderList.append(nodesInALevel)
                break
        
        return zigZagLevelOrderList
                
                

                
        
        
        