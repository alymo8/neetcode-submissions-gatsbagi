import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(x[0]**2 + x[1]**2, [x[0],x[1]]) for x in points]
        heapq.heapify(heap)
        res = []
        while k > 0:
            res.append(heapq.heappop(heap)[1])
            k -= 1
        return res