# https://leetcode.com/problems/swap-nodes-in-pairs/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        t = head
        while(t!= None and t.next != None):
            n = t.next.val
            t.next.val = t.val
            t.val = n
            
            t = t.next.next
            
        return head