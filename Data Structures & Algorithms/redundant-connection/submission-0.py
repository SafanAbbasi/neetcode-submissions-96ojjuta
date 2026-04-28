class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)
        # parent[i] will point to the parent of node i.
        # We use n + 1 because the nodes are 1-indexed.
        parent =[i for i in range(n + 1)]
        # rank[i] is used to keep the trees flat during union operations.
        rank = [1] * (n + 1)
        
        # The Find function with Path Compression
        def find(n):
            if parent[n] != n:
                # Path compression: update parent to the root directly
                parent[n] = find(parent[n])
            return parent[n]

       # The Union function with Union by Rank
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            
            # If they have the same parent, they are already connected!
            if p1 == p2:
                return False
            
            # Union by rank: attach the smaller tree under the larger tree
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
                
            return True

        # Process each edge
        for u, v in edges:
            # If union returns False, it means u and v were already connected.
            # We found our redundant connection!
            if not union(u, v):
                return [u, v]