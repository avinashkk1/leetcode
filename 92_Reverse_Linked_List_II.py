# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween2(self, head, numOfNodesToReverse):
        count = 0
        currNode = head
        prevNode = None
        
        while currNode and count < numOfNodesToReverse:
            nextNode = currNode.next 
            currNode.next = prevNode
            prevNode = currNode 
            currNode = nextNode
            count += 1
        
        return (prevNode, currNode)
        
        
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        currNode = head
        prevNode = None
        count = 1
        
        while currNode and count < left:
            prevNode = currNode
            currNode = currNode.next 
            count += 1
        
        if left == 1:
            head, currNode.next = self.reverseBetween2(currNode, right - left + 1)
        else:
            prevNode.next, currNode.next = self.reverseBetween2(currNode, right - left + 1)
            
        return head
        