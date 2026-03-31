# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        self.isValid = True

        if not root: 
            return True

        def dfs(root, lower_bound, upper_bound):

            if not root:
                return True
            
            if root.val <= lower_bound or  root.val >= upper_bound:
                self.isValid = False


            dfs(root.left, lower_bound, root.val )
            dfs(root.right, root.val, upper_bound)
        
        upper_bound = float("inf")  
        lower_bound = float("-inf") 
        dfs(root, lower_bound, upper_bound)


        return self.isValid

