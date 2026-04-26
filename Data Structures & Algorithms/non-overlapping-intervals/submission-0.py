class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])

        res = [intervals[0]]

        for i in range(1,len(intervals)):
            if res[-1][1] > intervals[i][0]:
                if intervals[i][1] < res[-1][1]:
                    res[-1] = intervals[i]
                else:
                    continue
            else:
                res.append(intervals[i])

        return len(intervals) - len(res)