# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        head1, head2 = head, head.next
        tail1, tail2 = head1, head2
        curr = head2.next
        
        while curr:
            tail1.next = curr
            tail1 = curr
            curr = curr.next
            
            if curr:
                tail2.next = curr
                tail2 = curr
                curr = curr.next 
        
        tail1.next = head2
        tail2.next = None
        return head
            
            
            
        
        
        