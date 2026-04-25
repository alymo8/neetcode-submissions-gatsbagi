class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        new_interval = newInterval
        for i, interval in enumerate(intervals):
            if new_interval[1] < interval[0]:
                res.append(new_interval)
                res += intervals[i:]
                return res
            elif new_interval[0] > interval[1]:
                res.append(interval)
            else:
                new_interval = [min(interval[0], new_interval[0]), max(interval[1], new_interval[1])]
        res.append(new_interval)
        return res