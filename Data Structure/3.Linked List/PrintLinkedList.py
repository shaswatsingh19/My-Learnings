# https://workat.tech/problem-solving/practice/print-linked-list
"""
This is the ListNode class definition

class ListNode:
	def __init__(self, data=0, next=None):
		self.data = data
		self.next = next

"""


class Solution:
	def printLinkedList(self, head: ListNode) -> None:
		# add your logic here
		t  = head
		while(t != None):
			print(t.data,end=" ")
			t = t.next
		


