# https://leetcode.com/problems/remove-linked-list-elements/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], v: int) -> Optional[ListNode]:
        
        while(head and head.val == v):
            head = head.next
        
        d = head
        while(d != None and d.next != None):
            if d.next.val == v:
                d.next = d.next.next
                continue
                
            
            d = d.next
            
        return head