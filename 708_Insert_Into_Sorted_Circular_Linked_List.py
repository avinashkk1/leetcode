"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        insertNode = Node(insertVal)
        
        if head is None:
            insertNode.next = insertNode
            return insertNode
        
        if head.next is None:
            head.next = insertNode
            insertNode.next = head
            return head
        
        prev, curr = head, head.next
        
        while prev.next != head:
            if prev.val <= insertVal <= curr.val:
                break
            
            if prev.val > curr.val and (insertVal > prev.val or insertVal < curr.val):
                break
            
            prev, curr = curr, curr.next 
        
        prev.next = insertNode
        insertNode.next = curr
        return head
        