"""
This is the Node class definition

class Node:
	def __init__(self, data=0, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

"""

# https://workat.tech/problem-solving/practice/binary-tree-inorder-traversal
class Solution:
	def getInorderTraversal(self, root: Optional[Node]) -> List[int]:
		l =[]
		self.inorder(root,l)
		return l
	
	def inorder(self,root,l):
		if root:
			self.inorder(root.left,l)
			l.append(root.data)
			self.inorder(root.right,l)
			


