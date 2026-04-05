class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []

        freqs = {}
        for i in range(len(nums)):
            cur = nums[i]
            freqs[cur] = freqs.get(cur, 0) + 1
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in freqs.items():
            buckets[freq].append(num)

        for i in range(len(nums), 0, -1):
            if buckets[i] != []:
                result.extend(buckets[i])
            if len(result) == k:
                return result


        # freqs = sorted(freqs.items(), key = lambda item: item[1], reverse = True)
        # keys = [key for key, value in freqs]
        # return keys[:k]