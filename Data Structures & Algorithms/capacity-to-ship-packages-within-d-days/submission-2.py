class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        best = 0
        while l <= r:
            mid = (l + r) // 2
            
            d = 1
            load = 0
            for weight in weights:
                if load + weight <= mid:
                    load += weight
                else:
                    d += 1
                    load = weight
            if d <= days:
                best = mid
                r = mid - 1
            elif d > days:
                l = mid + 1
        return best


