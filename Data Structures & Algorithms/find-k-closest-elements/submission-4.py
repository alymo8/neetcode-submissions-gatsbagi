import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # define array res of size k, start with empty
        # iterate on arr and start populating until size k reached
        # if size = k, compare abs differenc - new value with first index, 
        #    if smaller pop index 0 and add to end of arr, 
        #    keep going until we're not modifying res

        res = []
        for val in arr:
            if len(res) < k:
                res.append(val)
            else:
                if abs(res[0] - x) > abs(val - x):
                    res.pop(0)
                    res.append(val)
        return res
        


            
