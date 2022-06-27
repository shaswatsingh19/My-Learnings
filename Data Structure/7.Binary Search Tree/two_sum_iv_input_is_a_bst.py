# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        li = []
        def inorder(root):
            
            if root.left:
                inorder(root.left)
            li.append(root.val)
            if root.right:
                inorder(root.right)
                
                
        inorder(root)
        print(li)
        i = 0
        j = len(li)-1
        
        while i<j:
            s = li[i] + li[j]
            if s < k:
                i+=1
            elif s > k:
                j-=1
            else:
                return True
            
        return False

    
        '''
        bfs
        q = deque()
        
        q.append(root)
        di = {}
        while q:
            popped = q.popleft()
            if k-popped.val in di:
                return True
            else:
                di[popped.val] = 1
                
            if popped.left:
                q.append(popped.left)
            if popped.right:
                q.append(popped.right)
                
        return False
        '''
        
        '''
        dfs
        di = {}
        
        def pre(root):
            
            if root is None:
                return False
            if k-root.val in di:
                return True
            else:
                di[root.val] = 1
            print(di)
                
            return pre(root.left) or pre(root.right)
            
        
        return pre(root)
        '''