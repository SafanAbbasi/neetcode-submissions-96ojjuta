class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        edges = collections.defaultdict(list)

        # need to go through every edge ,not every node

        for start, end in tickets:
            edges[start].append(end)

        # sort all the edges
        for start in edges:
            edges[start].sort(reverse=True)


        res = []


        def dfs(airport):
            while edges[airport]:
                nei = edges[airport].pop()

                dfs(nei)

            res.append(airport)
        
        dfs("JFK")

        return res[::-1]