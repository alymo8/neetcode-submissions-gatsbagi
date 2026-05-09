import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # define array res of size k, start with empty
        # iterate on arr and start populating until size k reached
        # if size = k, compare abs difference - new value with first index, 
        #    if smaller pop index 0 and add to end of arr, 
        #    keep going until we're not modifying res

        l = 0
        r = len(arr) - 1
        while r - l >= k:
            if abs(arr[l] - x) > abs(arr[r] - x):
                l += 1
            else:
                r -= 1
        return arr[l: r+1]
        


            
