from collections import deque
# https://leetcode.com/problems/symmetric-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        #bfs
        queue = deque()
        
        queue.append(root)        
        queue.append(root)
        
        while queue:
            r1 = queue.popleft()
            r2 = queue.popleft()
            
            
            if r1 is None and r2 is None:
                continue
            if (r1 is None or r2 is None):
                return False
            if (r1.val != r2.val):
                return False
                
            queue.append(r1.left)
            queue.append(r2.right)
            queue.append(r1.right)
            queue.append(r2.left)
            
        return True
        
        '''
        # dfs
        def mirror(a,b):
            if a is None and b is None :
                return True
            if a is None or b is None :
                return False
            
            return a.val == b.val and mirror(a.right , b.left ) and mirror(a.left,b.right)
        
        
        return mirror(root,root)
        '''