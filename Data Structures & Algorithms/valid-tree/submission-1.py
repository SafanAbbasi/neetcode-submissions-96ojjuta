class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # list of edges

        adj = defaultdict(list)

        # need both directions since undirected
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        q = collections.deque([(0, -1)])

        visited = set([0])


        while q:

            node, parent = q.popleft()

            for neighbor in adj[node]:
                if neighbor == parent:
                    continue  # skip where we came from
                if neighbor in visited:
                    return False
                
                q.append((neighbor, node))
                visited.add(neighbor)
            
        
        return len(visited) == n