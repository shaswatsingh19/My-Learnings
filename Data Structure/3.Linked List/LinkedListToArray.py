"""
This is the ListNode class definition

class ListNode:
	def __init__(self, data=0, next=None):
		self.data = data
		self.next = next

"""
# https://workat.tech/problem-solving/practice/linked-list-to-array

class Solution:
	def linkedListToArray(self, head: ListNode) -> List[int]:
		arr = []
		
		t  = head
		while(t!=None):
			arr.append(t.data)
			t = t.next
		return arr


