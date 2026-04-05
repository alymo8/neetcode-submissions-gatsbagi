class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []

        freqs = {}
        for i in range(len(nums)):
            cur = nums[i]
            freqs[cur] = freqs.get(cur, 0) + 1
        freqs = sorted(freqs.items(), key = lambda item: item[1], reverse = True)
        keys = [key for key, value in freqs]
        return keys[:k]