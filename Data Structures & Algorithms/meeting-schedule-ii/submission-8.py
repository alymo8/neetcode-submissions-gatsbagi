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
        endtimes = []
        heapq.heappush(endtimes, intervals[0].end)
        # 579, 918, 

        for i in range(1,len(intervals)):
            if intervals[i].start >= endtimes[0]:
                heapq.heappop(endtimes)
            heapq.heappush(endtimes, intervals[i].end)
    
        return len(endtimes)
                    


        