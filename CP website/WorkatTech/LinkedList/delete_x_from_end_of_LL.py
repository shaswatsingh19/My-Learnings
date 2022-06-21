"""
This is the ListNode class definition

class ListNode:
	def __init__(self, data=0, next=None):
		self.data = data
		self.next = next

"""


class Solution:
	def removeXthNodeFromEnd(self, head: ListNode, x: int) -> ListNode:
		# add your logic here
		
		l=0
		temp = head
		while(temp!= None):
			l += 1
			temp=temp.next
		
		if x==l:
			return head.next
		
		x = l-x-1
		
		
		temp = head
		while(x>0):
			temp = temp.next
			x-=1
			
				
			
		if temp is not None and temp.next is not None:
			temp.next = temp.next.next
		
		return head