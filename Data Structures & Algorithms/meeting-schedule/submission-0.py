"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        
        intervals.sort(key=lambda x: x.start)

        # sort by start time
        # if any end time of the current interval is greater than the start time of the next interval, then false

        for idx, interval in enumerate(intervals):
            if idx+1 < len(intervals) and interval.end > intervals[idx+1].start:
                return False

        return True