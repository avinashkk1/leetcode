# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findMiddleNode(self, head):
        slowPointer, fastPointer = head, head
        
        while fastPointer.next and fastPointer.next.next:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next
        
        return slowPointer
    
    def reverseLinkedList(self, head):
        currNode, prevNode = head, None
        
        while currNode:
            nextNode = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode
        
        return prevNode
        
        
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next is None:
            return True
        
        middleNode = self.findMiddleNode(head)
        middleNext = middleNode.next
        
        secondHalfHead = self.reverseLinkedList(middleNext)
        middleNode.next = secondHalfHead
        
        currNode1, currNode2 = head, secondHalfHead
        isPalindromeFlag = True
        while currNode1 and currNode2 and currNode1 != secondHalfHead:
            if currNode1.val != currNode2.val:
                isPalindromeFlag = False
                break
            currNode1 = currNode1.next
            currNode2 = currNode2.next
        
        secondHalfHead = self.reverseLinkedList(secondHalfHead)
        middleNode.next = secondHalfHead
        return isPalindromeFlag
        
        
        
        
        
        
    def isPalindrome1(self, head: Optional[ListNode]) -> bool:
        # O(n) space 
        
        linkedListEle = []
        
        currNode = head
        while currNode:
            linkedListEle.append(currNode.val)
            currNode = currNode.next
        
        n = len(linkedListEle)
        for i in range(n // 2):
            if linkedListEle[i] != linkedListEle[n - 1 - i]:
                return False
        
        return True
        
        