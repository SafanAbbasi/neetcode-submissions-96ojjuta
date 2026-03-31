# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# every tree will be a binary search tree
# keep going left when possible and counting
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.smallcount = 0
        self.kth_value = root.val

        def inorder(root):
            if not root:
                return 

            inorder(root.left)
            self.smallcount += 1

            if self.smallcount == k:
                self.kth_value = root.val



            inorder(root.right)

    # start from smallest, then 2nd smallest, then 3rd
    # eseential in-order traversal. left, then node, then right

        
        inorder(root)

        return self.kth_value