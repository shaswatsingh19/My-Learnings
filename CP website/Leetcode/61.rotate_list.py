# https://leetcode.com/problems/rotate-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        n=0
        curr = head
        while curr:
            n+=1
            curr = curr.next
        k = k % n
        
        p1 = head
        p2 = head
        while k:
            p2 = p2.next
            k-=1
            
        while p2.next:
            p1=p1.next
            p2=p2.next
            
        p2.next = head
        head = p1.next
        p1.next = None
        
        return head
        
        
        