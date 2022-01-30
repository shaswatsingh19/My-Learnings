"""
This is the ListNode class definition

class ListNode:
	def __init__(self, data=0, next=None):
		self.data = data
		self.next = next

"""
# https://workat.tech/problem-solving/practice/intersection-two-linked-lists

class Solution:
	def getIntersectionNode(self, a: ListNode, b: ListNode) -> Optional[ListNode]:

#       O(N) Time O(1) Space	

		t1 = a
		t2 = b
		while(t1 != None and t2!= None):
			if(t1==t2):return t1
			t1= t1.next
			t2= t2.next
			if(t1==None):
				t1 = b
			elif (t2==None):
				t2 = a
				
		return None
		
		
		
# -------------------------------------------------------------
#       O(N) Time O(1) Space
# 		d1 = a
# 		d2 = b
# 		l1 = 0
# 		l2 = 0
# 		while(d1 != None):
# 			l1+=1
# 			d1 = d1.next
			
# 		while(d2 != None):
# 			l2+=1
# 			d2 = d2.next
		
# 		d = l2-l1
		
# 		d = abs(d)
# 		d1 = a
# 		d2 = b
# 		if(l1>l2):
# 			while(d>0):
# 				d1 = d1.next
# 				d-=1
# 		else:
# 			while(d>0):
# 				d2= d2.next
# 				d-=1
		
# 		while(d1 != None or d2!= None):
# 			if(d1==d2):
# 				return d1
# 			d1 = d1.next
# 			d2 = d2.next
			
# 		return None
				
				
# 	    O(N+M) time and O(N+M) Space
# 		di = {}
# 		if(a == None or b == None):
# 			return None

# 		while( a != None ):
# 			di[a] = 1
# 			a =a.next

# 		while(b!=None):
# 			if(b in di):
# 				return b
# 			b = b.next
# 		return None

#-----------------------------------------------------------------------
		
# 		O(N*M) time 
# 		curr  = b
			
# 		while ( curr!=None):
# 			temp = a
# 			while(temp!=None):
# 				if(curr == temp):
# 					return curr
# 				temp = temp.next
# 			curr = curr.next
			
# 		return None
		
