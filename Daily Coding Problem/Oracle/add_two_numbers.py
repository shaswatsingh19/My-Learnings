# https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Created dummy node so that I can change the l1 and l2 and 
        # store there value in it 
        dummy = ListNode(0)
        curr  = dummy
        carry = 0
        s = 0
        while l1 or l2:
            
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            s = v1 + v2 + carry
            
            newNode  = ListNode(s%10)
            carry = s//10
            curr.next = newNode
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        # important step if carry is greater than 1
        if carry:
            newNode = ListNode(carry)
            curr.next = newNode
        return dummy.next
            
            
            