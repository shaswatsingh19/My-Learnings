# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
# Bottom up approach
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        
        if root is None :
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        return max(left,right)+1
        
        
# Top Down approach
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
        
#         return self.pre(root,0,0)
    
#     def pre(self,root,c,m):
        
        
#         if root is None :
#             m = max(c,m)
#             c = 0
#             return m
        
#         if root:
#             c+=1
#             m = max(m,self.pre(root.left,c,m),self.pre(root.right,c,m))
            
#         return m
        