"""
This is the ListNode class definition

class ListNode:
	def __init__(self, data=0, next=None):
		self.data = data
		self.next = next

"""


class Solution:
	def removekthElement(self, head: ListNode, k: int) -> ListNode:
		# add your logic here
		
		if k == 1:
			head = head.next
		else:
			t = head
			for i in range(k-2):
				t = t.next
				if t is None:# k > length of element in LL
					break
				
			if t != None:
				n = t.next
				t.next = n.next
				n.next = None
			
		while(head!=None):
			print(head.data,end=' ')
			head = head.next


