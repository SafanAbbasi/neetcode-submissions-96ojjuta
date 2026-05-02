class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # so keep track of costs 
        # cheapest cost as you go along path = Dijkstra 
        # also track stops

        adj = collections.defaultdict(list)

        for a_src, a_dest, cost in flights:
            adj[a_src].append((cost, a_dest)) 

        minheap = [[0,src, 0]] #cost, airport, stops # starting point

        while minheap: 

            cost, airport, stops = heapq.heappop(minheap)

            if airport == dst:
                return cost

            if stops <= k:
                for next_cost , dest in adj[airport]: #all the connected places to this currnet airport 
                    heapq.heappush(minheap, (cost+ next_cost, dest, stops + 1))
        
        return -1