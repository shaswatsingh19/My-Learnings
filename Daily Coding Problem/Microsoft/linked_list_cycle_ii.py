# https://leetcode.com/problems/linked-list-cycle-ii/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None

        curr = head
        
        while curr != fast:
            curr= curr.next
            fast= fast.next
        
        return curr
        
        
        
#         di = {}
#         curr = head
        
#         while curr:
            
#             if curr not in di:
#                 di[curr] = 1
#             else:
#                 return curr
            
#             curr = curr.next
            
            
#         return None