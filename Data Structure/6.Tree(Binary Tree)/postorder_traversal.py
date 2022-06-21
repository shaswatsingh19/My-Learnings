"""
This is the Node class definition

class Node:
	def __init__(self, data=0, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

"""

# https://workat.tech/problem-solving/practice/binary-tree-postorder-traversal/
class Solution:
	def getPostorderTraversal(self, root: Optional[Node]) -> List[int]:
		# add your logic here
		
		l = []
		self.post(root,l)
		return l
	
	def post(self,root,l):
		
		if root:
			self.post(root.left,l)
			self.post(root.right,l)
			l.append(root.data)


