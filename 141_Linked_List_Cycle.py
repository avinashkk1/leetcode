# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        
        slowPointer = head
        fastPointer = head.next
        
        while slowPointer != fastPointer:
            if fastPointer is None or fastPointer.next is None:
                return False
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next 
        
        return True
        