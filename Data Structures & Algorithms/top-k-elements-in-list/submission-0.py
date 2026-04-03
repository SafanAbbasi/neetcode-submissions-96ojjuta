from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #most frequent elements, not the biggest
        # get freq count using dict
        # once I have the count then I can iterate through the dict and fix the most freq

        count = Counter(nums)
        k_freq = []

        for key, value in count.items():
            k_freq.append((key,value))

        k_freq.sort(key=lambda x: (-x[1], x[0]) )

        return [num for num, count in k_freq[:k]]
