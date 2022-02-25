# https://leetcode.com/problems/linked-list-cycle/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = head
        f = head
        
        while (f!= None and f.next != None):
            s = s.next
            f = f.next.next
            
            if s==f:
                return True
            
        return False
        
#         di = {}
        
#         t  = head
#         while t:
#             if t not in di:
#                 di[t] = 1
#             elif t in di:
#                 return True
            
#             t  = t.next
            
#         return False