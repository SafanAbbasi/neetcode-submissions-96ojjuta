# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.issubroot = False


        def dfs(root):
            
            if not root or not subRoot:
                return
            
            if root.val == subRoot.val:
                if sameTree(root, subRoot):
                    self.issubroot = True

            dfs(root.left)
            dfs(root.right)

        def sameTree(root, subRoot):

            if not root and not subRoot:
                return True

            if root is None and subRoot:
                return False

            if subRoot is None and root:
                return False

            if root.val != subRoot.val:
                return False

            return sameTree(root.left, subRoot.left) and sameTree(root.right, subRoot.right)

        
        dfs(root)

        return self.issubroot