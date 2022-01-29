"""
This is the ListNode class definition

class ListNode:
	def __init__(self, data=0, next=None):
		self.data = data
		self.next = next

"""


class Solution:
	def reverseLinkedList(self, head: ListNode) -> ListNode:
		# add your logic here
		curr = head
		prev = None
		next = None
		
		while(curr!=None):
			next = curr.next
			curr.next = prev
			prev = curr
			curr = next
		
		head = prev
		return head