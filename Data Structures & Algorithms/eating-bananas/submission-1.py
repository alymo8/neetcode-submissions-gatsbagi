import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search the solution
        # between max(arr) and h / len(piles)

        l, r = 1, max(piles)
        res = -1

        while l <= r:
            mid = (l + r) // 2
            hours = sum(math.ceil(piles[i] / mid) for i in range(len(piles)))
            if hours <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res

                