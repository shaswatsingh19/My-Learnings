"""
This is the Node class definition

class Node:
	def __init__(self, data=0, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

"""
# https://workat.tech/problem-solving/practice/binary-tree-preorder-traversal/

class Solution:
	def getPreorderTraversal(self, root: Optional[Node]) -> List[int]:
		# add your logic here
		l = []
		self.preorder(root,l)
		
		return l
	
	def preorder(self,root,l):
		
		if (root):
			l.append(root.data)
			self.preorder(root.left,l)
			self.preorder(root.right,l)
			
		
		


