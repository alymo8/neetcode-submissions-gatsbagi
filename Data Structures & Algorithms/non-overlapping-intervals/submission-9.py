class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # ____________ ______ ______
        # ________________ 
        # sort, remove those who are overlapping and end last
        intervals.sort(key = lambda x: x[1])
        last = intervals[0][1]
        res = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < last:
                res += 1
            else:
                last = intervals[i][1]
        return res