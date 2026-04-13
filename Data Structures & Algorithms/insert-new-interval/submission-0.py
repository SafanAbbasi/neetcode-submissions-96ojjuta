class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []

        for idx in range(len(intervals)):

            if intervals[idx][1] < newInterval[0]: # end time is less than new interval's start value.
                output.append(intervals[idx])
            elif intervals[idx][0] > newInterval[1]: # start time greater than new intervals end value. 
                output.append(newInterval)
                output += intervals[idx:]
                return output
            else:
                newInterval = [min(newInterval[0], intervals[idx][0]),
                   max(newInterval[1], intervals[idx][1])]
        
        output.append(newInterval)
        return output