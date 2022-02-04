# https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        temp = dummy
        
        c = 0
        while(l1!=None or l2!=None):
            s = 0
            d = ListNode()
            if(l1!=None):
                s += l1.val
                l1 = l1.next
            if(l2!=None):
                s += l2.val
                l2 = l2.next
            
            s += c
            d.val = s%10
            c = s//10
            
            temp.next = d
            temp = temp.next

            
        if(c>0):
            d = ListNode(c)
            temp.next = d
            
        return dummy.next
            