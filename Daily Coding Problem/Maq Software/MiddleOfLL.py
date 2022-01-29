"""
This is the ListNode class definition

class ListNode:
	def __init__(self, data=0, next=None):
		self.data = data
		self.next = next

"""

# https://workat.tech/problem-solving/practice/middle-element-linked-list
class Solution:
	def getMiddleElementOfLinkedList(self, head: ListNode) -> int:
		# add your logic here
		f = head
		s = head

		while(f.next!=None and f.next.next != None):
			s = s.next
			f = f.next.next
			
		return s.data

