# https://workat.tech/problem-solving/practice/kth-element-linked-list/editorial
"""
This is the ListNode class definition

class ListNode:
	def __init__(self, data=0, next=None):
		self.data = data
		self.next = next

"""


class Solution:
	def kthElement(self, head: ListNode, k: int) -> ListNode:
		# add your logic here
		t = head
		for i in range(k-1):
			t = t.next
		return t
			