"""
This is the ListNode class definition

class ListNode:
	def __init__(self, data=0, next=None):
		self.data = data
		self.next = next

"""

# https://workat.tech/problem-solving/practice/linked-list-palindrome/
class Solution:
	def isPalindrome(self, list: ListNode) -> bool:
		# add your logic here
		
		mid = self.middle(list)
		rev = self.reverse(mid.next)
		
		while(rev != None):
			if (rev.data != list.data):
				return 0
			rev = rev.next
			list = list.next
		return 1
		
	def reverse(self,head):
		
		c = head
		n = None
		p = None
		while(c != None):
			n  = c.next
			c.next = p
			p = c 
			c = n
		head = p
		
		return head

		
	def middle(self,head):
		fast = ListNode()
		fast = head
		
		while(fast.next != None and fast.next.next != None):
			head = head.next
			fast = fast.next.next;
		return head