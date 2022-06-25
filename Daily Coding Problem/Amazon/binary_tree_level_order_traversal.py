# https://leetcode.com/problems/binary-tree-level-order-traversal/
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        q.append(root)
        ans = []
        temp = []
        i=0
        
        while q:
            i = len(q)
            temp = []
            while i:
                root = q.popleft()
                temp.append(root.val)
                
                if root.left:
                    q.append(root.left)

                if root.right:
                    q.append(root.right)
                    
                i-=1
                
            ans.append(temp)
            
        return ans