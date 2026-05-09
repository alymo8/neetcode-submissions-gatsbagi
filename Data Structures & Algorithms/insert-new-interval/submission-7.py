class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # iterate on intervals while end < new[0]
        # cases: 
        #   no overlap
        #   overlap before
        #   overlap after
        #   overlap all of interval or multiple
        # consider: after insert of cur interval, 
        # need to update list and remove next intervals
        # use copy of list

        # detect place to insert (first interval when end <start )
        # manage overlaps by adding - not adding to result list
        result = []
        for i, interval in enumerate(intervals):
            if newInterval[0] > interval[1]:
                result.append(interval)
            elif newInterval[1] < interval[0]:
                result.append(newInterval)
                result += intervals[i:]
                return result
            else:
                newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]
        
        result.append(newInterval)
        
        return result


