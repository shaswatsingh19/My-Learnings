# https://leetcode.com/problems/binary-tree-inorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        return self.inorder(root,[])
    
    
    
    def inorder(self,root,l):
        
        if root:
            self.inorder(root.left,l)
            l.append(root.val)
            self.inorder(root.right,l)
            
            
        return l
        