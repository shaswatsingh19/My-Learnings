# https://leetcode.com/problems/merge-two-sorted-lists/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        h = ListNode(0)
        t = h 
        
        while (l1 and l2):
            if l1.val <= l2.val:
                h.next = l1
                h = l1
                l1 = l1.next
            else:
                h.next = l2
                h = l2
                l2 = l2.next
                
        if l1:
            h.next = l1
        if l2:
            h.next = l2
            
        return t.next
        
        

        
        
        
        
        
        
#         dummy = ListNode(0)
#         t = dummy 
        
#         while(list1 and list2):
#             d = ListNode(0)
            
#             if list1.val <= list2.val:
#                 d.val = list1.val

#                 list1 = list1.next
                
#             else:
#                 d.val = list2.val
#                 list2 = list2.next
#             t.next = d
#             t = d
        
#         if list1 != None:
#             t.next = list1
#         if list2 != None:
#             t.next = list2
#         return dummy.next
        