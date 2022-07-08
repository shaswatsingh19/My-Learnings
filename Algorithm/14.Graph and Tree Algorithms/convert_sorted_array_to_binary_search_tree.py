# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/solution/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        # [-5,-3,-2,-1,0,1,2,3,4,5,6]
        # mid = 11/2 = 5
        
        def binary(l,r):
            
            if l>r:
                return None
            
            mid = (l+r)//2
            
            root = TreeNode(nums[mid])
            
            root.left = binary(l,mid-1)
            root.right = binary(mid+1,r)
            
            return root
        
        return binary(0,len(nums)-1)
        