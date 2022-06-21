# https://leetcode.com/problems/odd-even-linked-list/solution/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None or head.next is None or head.next.next is None:
            return head
        
        odd , h1 = head , head
        even , h2 = head.next , head.next
        
        prev = None
        while odd and even:
            odd.next = odd.next.next
            prev = odd 
            odd = odd.next
            if even.next is None :
                break
            even.next = even.next.next
            even = even.next
            
        if odd:
            odd.next = h2
        else:
            prev.next = h2
            
        return h1
        