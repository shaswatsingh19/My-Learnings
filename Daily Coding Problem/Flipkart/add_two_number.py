"""
This is the ListNode class definition

class ListNode:
	def __init__(self, data=0, next=None):
		self.data = data
		self.next = next

"""


# https://workat.tech/problem-solving/practice/add-numbers-lists
class Solution:
	def addTwoNumbers(self, firstList: ListNode, secondList: ListNode) -> ListNode:
		# add your logic here
		
		s = firstList
		t = secondList
		ans  = 0
		c = 0
		result = ListNode(-1)
		temp = result
		while(s!= None or t != None):
			ans = 0
			if s is not None:
				ans += s.data
				s  = s.next
				
			if t is not None:
				ans += t.data
				t = t.next
				
			ans += c
			c = ans//10
			dummy = ListNode(ans%10)
			temp.next = dummy
			temp = temp.next
			
		if c>0:
			dummy = ListNode(c)
			temp.next = dummy
			temp = temp.next
			
		return result.next