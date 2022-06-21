# https://workat.tech/problem-solving/practice/print-reversed-linked-list
"""
This is the ListNode class definition

class ListNode:
	def __init__(self, data=0, next=None):
		self.data = data
		self.next = next

"""


class Solution:
	def printLinkedListReverse(self, head: ListNode) -> None:
		# add your logic here
# 		curr = head
# 		next = None
# 		prev = None
# 		while(curr != None):
# 			next = curr.next
# 			curr.next = prev
# 			prev = curr
# 			curr = next
			
# 		head = prev
		
# 		temp = head
# 		while(temp!=None):
# 			print(temp.data,end=' ')
# 			temp = temp.next
		
		if(head.next != None):
			self.printLinkedListReverse(head.next)
			
		print(head.data,end=' ')

