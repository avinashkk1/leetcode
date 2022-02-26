# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        dummyHead.next = head
        
        fastNode = slowNode = dummyHead
        
        for i in range(n + 1):
            fastNode = fastNode.next
        
        while fastNode:
            fastNode = fastNode.next
            slowNode = slowNode.next
        
        slowNode.next = slowNode.next.next
        return dummyHead.next 
    
            
            
        