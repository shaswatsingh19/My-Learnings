# https://leetcode.com/problems/binary-tree-postorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.post_order(root,[])
    
    
    
    def post_order(self,root,l):
        
        if root == None:
            return 
        
        if root:
            self.post_order(root.left,l)
            self.post_order(root.right,l)
            
            l.append(root.val)
            
            
        return l
        