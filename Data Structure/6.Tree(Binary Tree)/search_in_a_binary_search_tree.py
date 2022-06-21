# https://leetcode.com/problems/search-in-a-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        while root is not None and root.val != target:
            
            if root.val > target:
                root = root.left
            else:
                root = root.right
        return root
    
        
#         if root is None or root.val == target :
#             return root
        
#         if target < root.val:
            
#             return self.searchBST(root.left,target)
#         else:
#             return self.searchBST(root.right,target)
        
#         return root