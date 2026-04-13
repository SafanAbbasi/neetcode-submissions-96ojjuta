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

        minheap = []
        intervals.sort(key=lambda x: x.start)

        for i in range( len(intervals)):

            if minheap and intervals[i].start >= minheap[0]:
                heapq.heappop(minheap) # reuse a room 
            
            heapq.heappush(minheap, intervals[i].end) # pushing means occupying a room
        return len(minheap)


### sweeping line algorithm

        mp = defaultdict(int)
        for i in intervals:
            mp[i.start] += 1
            mp[i.end] -= 1
        prev = 0
        res = 0
        for i in sorted(mp.keys()):
            prev += mp[i]
            res = max(res, prev)
        return res