"""
This is the ListNode class definition

class ListNode:
	def __init__(self, data=0, next=None):
		self.data = data
		self.next = next

"""

# https://workat.tech/problem-solving/practice/delete-node-linked-list
class Solution:
	def deleteNode(self, node: ListNode) -> None:
		
		next  = node.next
		node.data = next.data
		node.next = next.next
