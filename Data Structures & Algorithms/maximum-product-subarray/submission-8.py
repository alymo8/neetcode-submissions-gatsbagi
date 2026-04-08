class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        curmax = nums[0]
        curmin = nums[0]

        for num in nums[1:]:
            tempmin = min(num, curmin * num, curmax * num)
            curmax = max(num, curmin * num, curmax * num)
            curmin = tempmin

            result = max(curmax, result)

        return result
