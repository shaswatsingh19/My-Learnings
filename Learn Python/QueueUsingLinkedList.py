"""
class ListNode:
	def __init__(self, data=0, next=None):
		self.data = data
		self.next = next
"""


class Queue:
	def __init__(self, capacity=0):
		self.f = None
		self.b = None
		self.s = 0

	def isEmpty(self) -> bool:
		if(self.f == None and self.b == None):
			return True
		return False
		 

	def size(self) -> int:
		return self.s
		 

	def front(self) -> int:
		if(self.f == None):
			return -1
		return self.f.data
		  

	def back(self) -> int:
		if(self.b == None):
			return -1
		return self.b.data
		 

	def push(self, element: int) -> None:
		new_node = ListNode(element)
		if(self.b == None):
			self.f = new_node
			self.b = new_node
		else:
			self.b.next = new_node
			self.b = new_node
		self.s +=1
		 

	def pop(self) -> None:
		self.s -=1
		self.f = self.f.next
		if(self.f == None):
			self.b = self.b.next
			
