class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])

        # res = [intervals[0]]
        count = 0
        prev_end = intervals[0][1]

        for i in range(1,len(intervals)):
            if prev_end > intervals[i][0]:
                count+=1
                if intervals[i][1] < prev_end:
                    prev_end = intervals[i][1]
                else:
                    continue
            else:
                prev_end = intervals[i][1]

        return count