"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #  ______
        #    ________
        # _____
        #              _________
        #                    ______________
        #                          _____________

        # sort by start time,
        # if overlap with all rooms, then add one more room
        # each room tracks its end time
        # rooms = list[int]
        # return len(rooms)
        if len(intervals) == 0:
            return 0
        
        intervals.sort(key = lambda x: x.start)
        rooms = [intervals[0].end]
        
        for i in range(1, len(intervals)):
            interval = intervals[i]
            min_index = rooms.index(min(rooms))
            if rooms[min_index] <= interval.start:
                rooms[min_index] = interval.end
            else:
                rooms.append(interval.end)
        return len(rooms)
