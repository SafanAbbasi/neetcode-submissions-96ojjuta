class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key=lambda x: x[0])
        
        for interval in intervals:

            if res and interval[0] <= res[-1][1]:
                mergedinterval = [min(res[-1][0], interval[0]), max(res[-1][1], interval[1]) ]
                res.pop()
                res.append(mergedinterval)
            else:
                res.append(interval)

        return res