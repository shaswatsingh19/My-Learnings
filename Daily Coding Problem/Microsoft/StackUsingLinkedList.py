"""
class ListNode:
	def __init__(self, data=0, next=None):
		self.data = data
		self.next = next
"""

# https://workat.tech/problem-solving/practice/implement-stack-linked-list

class Stack:
	def __init__(self, capacity=0):
		self.capacity = capacity
		self.s = 0
		self.t = -1
		self.head = None
		
		

	def isEmpty(self) -> bool:
		if (self.head == None):
			return True
		return False
			
		
	
	def top(self) -> int:
		if(self.head == None):
			return -1
		return self.head.data
		
	def size(self) -> int:
		return self.s
		

	def push(self, element: int) -> None:
		if(self.head == None):
			self.head = ListNode(element)
		
		else:
			new_node = ListNode(element)
			new_node.next = self.head
			self.head = new_node
		self.s += 1
		

	def pop(self) -> None:
		self.head = self.head.next
		self.s -=1
		


