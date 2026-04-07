class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        cursum = nums[0]

        for num in nums[1:]:
            cursum = max(num, cursum + num)
            result = max(cursum, result)
        return result