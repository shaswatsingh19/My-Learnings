# https://leetcode.com/problems/invert-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        
        self.swap(root)
        return root
        
        
        
    def swap(self,root):
        if (root == None):
            return
        
        self.swap(root.left)
        self.swap(root.right)
        
        t = TreeNode()
        t = root.left
        root.left = root.right
        root.right = t