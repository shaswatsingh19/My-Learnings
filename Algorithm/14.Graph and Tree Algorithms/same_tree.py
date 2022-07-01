# https://leetcode.com/problems/same-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # dfs
        if (p and q) and (p.val == q.val):
            l = self.isSameTree(p.left,q.left)
            r = self.isSameTree(p.right,q.right)
            return l and r
        elif p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        else:
            return False
        
        
        
#         if p is None and q is None:
#             return True
#         if p is None or q is None:
#             return False
        
#         def bfs(root):
#             ans = [root.val]
#             q = [root]
#             i = 0
#             while i<len(q):
#                 popped = q[i]
                
#                 if popped.left :
#                     q.append(popped.left)
#                     ans.append(popped.left.val)
#                 else:
#                     ans.append('placeholder')
                    
#                 if popped.right:
#                     q.append(popped.right)
#                     ans.append(popped.right.val)
#                 else:
#                     ans.append('placeholder')
                    
#                 i+=1
#             return ans
#         return bfs(p) == bfs(q)
        
        