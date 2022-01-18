# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subTreeMap = {} # (tuple of nodes in pre-order --> subTreeTypeID)
        subTreeTypeMap = {} # (subTreeTypeID --> List of root nodes of sub trees of this subTreeType)
        self.treeTypeId = 0
        
        def computeSubTreeMap(root):
            if not root:
                return -1
            
            preOrderTuple = (root.val, computeSubTreeMap(root.left), computeSubTreeMap(root.right))
            
            if preOrderTuple not in subTreeMap:
                subTreeMap[preOrderTuple] = self.treeTypeId
                self.treeTypeId += 1
            
            subTreeTypeId = subTreeMap[preOrderTuple]
                
            if subTreeTypeId in subTreeTypeMap:
                subTreeTypeMap[subTreeTypeId].append(root)
            else:
                subTreeTypeMap[subTreeTypeId] = [root]
            
            return preOrderTuple
        
        computeSubTreeMap(root)
        
        dupSubTreeTypes = []
        for rootNodesList in subTreeTypeMap.values():
            if len(rootNodesList) > 1:
                dupSubTreeTypes.append(rootNodesList[0])
        
        return dupSubTreeTypes
                

                
                    
            
        