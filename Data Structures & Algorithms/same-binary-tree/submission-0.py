# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.issame = True
        
        def dfs(p,q):
            if p is not None and q is not None:
                if p.val != q.val:
                    self.issame = False
                
                dfs(p.left, q.left)
                dfs(p.right, q.right)

            
            if p is None and q:
                self.issame = False

            
            if q is None and p:
                self.issame = False

        dfs(p,q)
        return self.issame