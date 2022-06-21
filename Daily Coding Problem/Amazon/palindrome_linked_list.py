# https://leetcode.com/problems/palindrome-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        
        mid = self.middle(head)
        
        tail = self.reverse(mid)
        
        while tail:
            if head.val != tail.val:
                return False
            head = head.next
            tail = tail.next
            
        return True
        
    def middle(self,head):
        slow = head
        fast = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow.next
    
    def reverse(self,head):
        
        c = head
        p = None
        n = None
        while c:
            n = c.next
            c.next = p
            p = c
            c = n
            
        head = p
        
        return p