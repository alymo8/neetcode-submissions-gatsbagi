import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search the solution
        # between max(arr) and h / len(piles)

        l = 1
        r = max(piles)
        res = -1
        while l <= r:
            hours = 0
            mid = (l + r) // 2
            for i in range(len(piles)):
                hours += math.ceil(piles[i] / mid)
            if hours <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
            

                