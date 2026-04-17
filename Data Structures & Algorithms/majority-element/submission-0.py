class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freqs = {}
        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1
        for k,v in freqs.items():
            if v >= len(nums) // 2:
                return k
        return -1