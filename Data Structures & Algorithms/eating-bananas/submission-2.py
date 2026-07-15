import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search the solution
        # between max(arr) and h / len(piles)

        l, r = 1, max(piles)
        result = 0

        while l <= r:
            mid = (l + r) // 2
            hours = sum(math.ceil(pile/mid) for pile in piles)
            if hours <= h:
                result = mid
                r = mid -1
            else:
                l = mid + 1
        return result

                