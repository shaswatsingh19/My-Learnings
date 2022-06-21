"""
This is the ListNode class definition

class ListNode:
	def __init__(self, data=0, next=None):
		self.data = data
		self.next = next

"""
# https://workat.tech/problem-solving/practice/merge-sorted-linked-list

class Solution:
	def mergeTwoSortedList(self, firstList: ListNode, secondList: ListNode) -> ListNode:
		# add your logic here
		dummy = ListNode()
		c1 = firstList
		c2 = secondList
		if(c1 == None or c2==None): 
			if(c1==None):
				return c2
			return c1
		
		if(c1.data <= c2.data):
			dummy = firstList
			p  = c1
			c1 = c1.next
		else:
			dummy = secondList
			p = c2
			c2 = c2.next
			
		while(c1 != None and c2 != None):
			if(c1.data <= c2.data):
				p.next  = c1
				c1 = c1.next
			else:
				p.next = c2
				c2 = c2.next
			p = p.next
		
		while(c1!=None):
			p.next  = c1
			c1 = c1.next
			p = p.next
		while(c2!=None):
			p.next = c2
			c2 = c2.next
			p = p.next
		return dummy
			
		
			
				
