# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # self.issame = True
        
        # def dfs(p,q):
        #     if p is not None and q is not None:
        #         if p.val != q.val:
        #             self.issame = False
                
        #         dfs(p.left, q.left)
        #         dfs(p.right, q.right)

            
        #     if p is None and q:
        #         self.issame = False

            
        #     if q is None and p:
        #         self.issame = False

        # dfs(p,q)

        # return self.issame

### Try BFS way

        self.issame = True

        p_queue = deque([p])
        q_queue = deque([q])
        

        while p_queue and q_queue:
            p_node = p_queue.popleft()
            q_node = q_queue.popleft()

            if p_node is None and q_node is None:
                continue

            if p_node is None and q_node:
                self.issame = False
                continue
            
            elif q_node is None and p_node:
                self.issame = False
                continue

            if p_node.val != q_node.val:
                self.issame = False

            if p_node is not None and q_node is not None:

                p_queue.append(p_node.left)
                p_queue.append(p_node.right)

                q_queue.append(q_node.left)
                q_queue.append(q_node.right)


        return self.issame




