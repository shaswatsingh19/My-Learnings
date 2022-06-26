# https://leetcode.com/problems/insert-into-a-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if not root:
            return TreeNode(val)
        
        
        if root.val > val:
            
            root.left  = self.insertIntoBST(root.left , val)
        else:
            root.right = self.insertIntoBST(root.right ,val)
            
        return root
    
    
#         if root is None:
#             return TreeNode(val)
        
#         temp = root
#         p = None
#         while root:
            
#             if root.val > val:
#                 p = root
#                 root = root.left
#             else:
#                 p = root
#                 root = root.right
                
#         newNode = TreeNode(val)
        
#         if p.val > val:
#             p.left = newNode
#         elif p.val < val:
#             p.right = newNode
        
#         return temp
            