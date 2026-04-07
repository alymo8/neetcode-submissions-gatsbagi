class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        cursum = nums[0]
        for i in range(1, len(nums)):
            cursum = max(nums[i], cursum + nums[i])
            result = max(result, cursum)

        return result
        