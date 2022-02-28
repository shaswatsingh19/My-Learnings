# https://leetcode.com/problems/binary-tree-preorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        return self.pre(root,[])
        
        
    def pre(self,root,l):
        
        if root is None:
            return 
        
        if root:
            l.append(root.val)
            self.pre(root.left,l)
            self.pre(root.right,l)
            
            
        return l