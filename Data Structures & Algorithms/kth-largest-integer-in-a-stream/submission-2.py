import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # self.maxheap = heapq.heapify(nums)
        self.nums = nums
        self.klargest = k
        heapq.heapify(self.nums)
        
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)

        while len(self.nums) > self.klargest:
            heapq.heappop(self.nums)

        return self.nums[0]