import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        maxheap = []
        output = []

        for i in range(len(nums)):
            heapq.heappush(maxheap, (-nums[i], i))

            if i >= k - 1:
                while maxheap[0][1] <= i - k:
                    heapq.heappop(maxheap)
                
                output.append(-maxheap[0][0])
        
        return output