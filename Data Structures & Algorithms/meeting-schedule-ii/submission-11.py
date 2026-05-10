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

        # sort by end time,
        # if overlap with all rooms, then add one more room
        # each room tracks its end time
        # rooms = list[int]
        # return len(rooms)
        if len(intervals) == 0: return 0

        intervals.sort(key = lambda x: x.start)

        rooms = [intervals[0].end]
        
        for i in range(1, len(intervals)):
            # go through rooms, see one room that ends before cur, 
            # update its end time
            min_index = rooms.index(min(rooms)) 
            if rooms[min_index] <= intervals[i].start:
                rooms[min_index] = intervals[i].end
                continue
            else:
                rooms.append(intervals[i].end)
        return len(rooms)

