# https://leetcode.com/problems/path-sum/ 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root:
            return
        
        targetSum =  targetSum - root.val
        if root.left is None and root.right is None and targetSum == 0:
            return True
        
        return self.hasPathSum(root.left,targetSum) or  self.hasPathSum(root.right,targetSum)    
    
        return False