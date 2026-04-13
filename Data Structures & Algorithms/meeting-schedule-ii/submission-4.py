"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # anytime there is a conflict in timings we would need an additional room
        # just need to track ending times and when meetings end
        if not intervals:
            return 0

        minheap = []
        intervals.sort(key=lambda x: x.start)

        for i in range( len(intervals)):

            if minheap and intervals[i].start >= minheap[0]:
                heapq.heappop(minheap)
            
            heapq.heappush(minheap, intervals[i].end)
        return len(minheap)
