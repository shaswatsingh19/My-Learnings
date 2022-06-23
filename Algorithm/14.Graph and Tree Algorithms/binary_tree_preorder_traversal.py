# https://leetcode.com/problems/binary-tree-preorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack , res = [root , ] , [] # in O(N) time and O(N) space
        while stack:
            root = stack.pop()
            if root:
                res.append(root.val)
                if root.right:
                    stack.append(root.right)
                if root.left:
                    stack.append(root.left)
        return res
                    
#         l = []
        
#         def pre(root):
#             if root:
#                 l.append(root.val)
#                 pre(root.left)
#                 pre(root.right)
                
                
#         pre(root)
#         return l
        

#         return self.pre(root,[])
        
        
#     def pre(self,root,l):
        
#         if root:
#             l.append(root.val)
#             self.pre(root.left,l)
#             self.pre(root.right,l)
            
            
#         return l
