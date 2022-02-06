# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        slow, fast = head, head
        
        while True:
            if fast is None or fast.next is None:
                return None
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                break
        
        meetingPoint = fast
        startPoint = head
        
        while startPoint != meetingPoint:
            startPoint = startPoint.next
            meetingPoint = meetingPoint.next
            
        return startPoint
        