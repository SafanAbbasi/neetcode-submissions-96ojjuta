import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stonesmax = [-s for s in stones]
        heapq.heapify(stonesmax)
        # have a max heap

        while len(stonesmax) > 1:
            large1 = -1 * heapq.heappop(stonesmax)
            large2 = -1 * heapq.heappop(stonesmax)

            if large1 == large2:
                continue
            elif large1 > large2: 
                large1 -= large2
                heapq.heappush(stonesmax, -1 * large1)

        if stonesmax:
            return -1 * stonesmax[0]
        else:
            return 0