class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        import heapq
        from collections import defaultdict 

        visited = set()

        minheap = [[0,k]] # time, node

        heapq.heapify(minheap)

        adj = defaultdict(list)

        for u,v,t in times: 
            adj[u].append((v, t)) # source -> (target, weight)


        while minheap:

            time, node = heapq.heappop(minheap)
            
            if node in visited:
                continue
            
            visited.add(node)

            
            if len(visited) == n:
                return time  # the last time you processed

            for nei, next_time in adj[node]:
                if nei in visited:
                    continue
                heapq.heappush(minheap, (time + next_time, nei))


        return -1