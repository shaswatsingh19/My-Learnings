"""
This is the ListNode class definition

class ListNode:
	def __init__(self, data=0, next=None):
		self.data = data
		self.next = next

"""

# https://workat.tech/problem-solving/practice/append-linked-lists
class Solution:
	def appendLists(self, list1: ListNode, list2: ListNode) -> ListNode:
		# add your logic here
		
		t = list1
		while(t.next!=None):
			t = t.next
			
		t.next  = list2
		
		while(list1 != None):
			print(list1.data,end=' ')
			list1= list1.next
			


