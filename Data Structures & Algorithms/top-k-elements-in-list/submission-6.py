class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1

        updated = sorted(freqs, key = lambda x: freqs[x], reverse = True)
        return updated[:k]