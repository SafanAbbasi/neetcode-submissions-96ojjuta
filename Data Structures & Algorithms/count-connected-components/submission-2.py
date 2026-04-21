class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = defaultdict(list)

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)


 

        visited = set()

        components = 0

        for i in range(n):
            if i not in visited:
                # found a new component, BFS from here
                components += 1
                # run BFS starting from this node
                 # adding everything you find to visited
                q = collections.deque([i])
                visited.add(i)
                
                while q:

                    node = q.popleft()

                    for connected in adj[node]:
                        
                        if connected not in visited:
                            visited.add(connected)
                        
                            q.append((connected))
                

        return components