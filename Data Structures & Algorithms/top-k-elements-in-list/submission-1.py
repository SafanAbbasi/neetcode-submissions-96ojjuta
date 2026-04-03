from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #most frequent elements, not the biggest
        # get freq count using dict
        # once I have the count then I can iterate through the dict and fix the most freq

        # freq = Counter(nums)
        # k_freq = []

        # for num, count in freq.items():
        #     k_freq.append([num,count])

        # k_freq.sort(key=lambda x: (-x[1], x[0]) )

    
        # return [num for num, count in k_freq[:k]]

        # for num, count in count.items():
        #     k_freq.append((num,count))

        # k_freq.sort(key=lambda x: (-x[1], x[0]) )

        # return [num for num, count in k_freq[:k]]


        # Min heap method
        freq = Counter(nums)

        minheap = []

        for key, value in freq.items():
            heapq.heappush(minheap, (value,key))

            if len(minheap) > k:
                heapq.heappop(minheap)

        res = []

        for i in range(k):
            res.append(heapq.heappop(minheap)[1])

        return res
