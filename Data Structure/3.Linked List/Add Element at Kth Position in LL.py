# https://workat.tech/problem-solving/practice/add-kth-element-linked-list
"""
This is the ListNode class definition

class ListNode:
	def __init__(self, data=0, next=None):
		self.data = data
		self.next = next

"""


class Solution:
	def addAtkthElement(self, head: ListNode, k: int, newElement: ListNode) -> ListNode:
		# add your logic here
		t = head
		if k == 1:
			newElement.next  = head
			head = newElement
		else:
			for i in range(k-2):
				t = t.next
			
			newElement.next = t.next
			t.next = newElement
			
		while(head!=None):
			print(head.data,end=' ')
			head = head.next
