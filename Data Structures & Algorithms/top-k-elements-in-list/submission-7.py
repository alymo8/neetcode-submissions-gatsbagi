class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1
        
        buckets =[[] for _ in range(len(nums)+1)]
        for num, freq in freqs.items():
            buckets[freq].append(num)

        res = []
        for i in range(len(buckets)-1, -1, -1):
            if buckets[i] != []:
                res.extend(buckets[i])
                if len(res) >= k:
                    return res[:k]
        return res[:k]