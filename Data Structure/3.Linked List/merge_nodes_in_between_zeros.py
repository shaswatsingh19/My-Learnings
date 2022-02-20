# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# https://leetcode.com/problems/merge-nodes-in-between-zeros/
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        p = head
        c  = head.next
        s=0
        while(c!= None):
            s += c.val
            
            if c.val == 0:
                c.val = s
                p.next = c
                p = c
                s =0
                
            c= c.next
            
            
        return head.next
        
#         dummy = ListNode(0)
#         t = dummy
#         s = 0
#         head = head.next
#         while(head!=None):
#             s += head.val
#             if head.val == 0:
#                 d = ListNode(s)
#                 t.next = d
#                 t  = d
#                 s = 0
            
#             head = head.next
            
#         return dummy.next