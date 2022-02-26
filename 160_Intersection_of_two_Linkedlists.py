# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        nodeA = headA
        nodeB = headB
        
        while nodeA != nodeB:
            nodeA = nodeA.next if nodeA else headB
            nodeB = nodeB.next if nodeB else headA
        
        return nodeA
        
        
        
    def getIntersectionNode1(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodeASet = set()
        
        currNode = headA
        
        while currNode:
            nodeASet.add(currNode)
            currNode = currNode.next 
        
        currNode = headB
        
        while currNode and currNode not in nodeASet:
            currNode = currNode.next
        
        return currNode
            
        