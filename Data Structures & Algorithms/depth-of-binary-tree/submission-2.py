# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0

        # leftdepth = self.maxDepth(root.left) + 1
        # rightdepth = self.maxDepth(root.right) + 1

        # return max(leftdepth, rightdepth)

        ### BFS approach

        if not root:
            return 0

        queue = deque([root])
        maxlevel = 0 # depth
        while queue:
            
            for item in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
            maxlevel += 1

        return maxlevel