class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        maxheap = []

        for point in points:

            distance = point[0]**2 + point[1]**2
            heapq.heappush(maxheap, (distance, point))

        # Pop k times — each pop gives the next closest
        result = []
        for _ in range(k):
            result.append(heapq.heappop(maxheap)[1])  # [1] gets the point, not the distance

        return result