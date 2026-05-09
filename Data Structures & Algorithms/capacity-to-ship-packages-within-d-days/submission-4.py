class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        while l <= r:
            mid = (l + r) // 2

            load = 0
            d = 1
            for weight in weights:
                if load + weight <= mid:
                    load += weight
                else:
                    d += 1
                    load = weight
            
            if d <= days:
                r = mid - 1
            else:
                l = mid + 1
        return l


