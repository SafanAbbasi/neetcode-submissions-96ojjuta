import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heapnum = [num for num in nums]
        heapq.heapify(heapnum)

        while len(heapnum) > k:
            heapq.heappop(heapnum)
        
        return heapnum[0]
