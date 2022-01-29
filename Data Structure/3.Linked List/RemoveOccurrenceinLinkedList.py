"""
This is the ListNode class definition

class ListNode:
	def __init__(self, data=0, next=None):
		self.data = data
		self.next = next

"""

# https://workat.tech/problem-solving/practice/remove-occurences-linked-list
class Solution:
	def removeOccurences(self, head: ListNode, key: int) -> ListNode:
		# add your logic here
		
		while(head != None and head.data == key ):
			head = head.next;
		
		c = head
		n = None
		p = None
		while(c!=None):
			n  = c.next
			while(n != None and n.data == key ):
				n = n.next
			c.next = n
			p = c
			c = n
		return head
		


