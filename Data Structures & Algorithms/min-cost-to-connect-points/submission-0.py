class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
    # Start from any point (say point 0)
    # Use a min heap to always pick the cheapest edge to an unvisited point
    # Add that point to the tree
    # Push all edges from the new point to unvisited points onto the heap
    # Repeat until all points are connected

    # One difference from your earlier problems: there's no adjacency list to build upfront. Every
    # point can connect to every other point, so you calculate the manhattan distance on the fly.


        minheap = [[0,0]] # cost, point_index
        visited = set() # don't want to revisit a point

        total_cost = 0 
        while minheap:
            
            cost, point_index = heapq.heappop(minheap)

            if point_index in visited:
                continue 
            
            visited.add(point_index)
            total_cost += cost

            if len(visited) == len(points):
                return total_cost

            for idx, point in enumerate(points):
                if idx == point_index:
                    continue
                
                dist = abs(points[point_index][0] - point[0]) + abs(points[point_index][1] - point[1])

                heapq.heappush(minheap, (dist,idx))


    
