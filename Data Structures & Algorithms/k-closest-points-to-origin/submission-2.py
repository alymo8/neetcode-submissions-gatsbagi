import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            x, y = point
            heap.append([x**2 + y**2, [x, y]])
        heapq.heapify(heap)
        res = []
        while k > 0:
            res.append(heapq.heappop(heap)[1])
            k -= 1
        return res