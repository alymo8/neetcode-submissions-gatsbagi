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
        if intervals == []:
            return 0
        intervals.sort(key = lambda x: x.start)
        endtimes = [intervals[0].end]
        # 579, 918, 

        for i in range(1,len(intervals)):
            add_room = True
            assign_room = -1
            interval_difference = float('inf')
            for j in range(len(endtimes)):
                if intervals[i].start >= endtimes[j]:
                    add_room = False
                    if intervals[i].start - endtimes[j] < interval_difference:
                        interval_difference = intervals[i].start - endtimes[j]
                        assign_room = j
            if add_room:
                endtimes.append(intervals[i].end)
            else:
                endtimes[assign_room] = intervals[i].end
        return len(endtimes)
                    


        