"""
This is the ListNode class definition

class ListNode:
	def __init__(self, data=0, next=None):
		self.data = data
		self.next = next

"""
# https://workat.tech/problem-solving/practice/remove-duplicates-sorted-linked-list/

class Solution:
	def removeDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
		# add your logic here
		
		c = head
		
		while(c != None and c.next != None):
			while(c.next != None and c.data == c.next.data):
				c.next = c.next.next
			c = c.next
			
		return head