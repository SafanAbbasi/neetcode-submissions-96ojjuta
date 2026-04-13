class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        overlap = 0

        intervals.sort(key=lambda start: start[0])

        for i in range( len(intervals) - 1):

            if intervals[i+1][0] < intervals[i][1]: # if the next intervals start time is less than previous intervals end time
                overlap += 1
                intervals[i+1][1] = min(intervals[i][1], intervals[i+1][1])


        return overlap