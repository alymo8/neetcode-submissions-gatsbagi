class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]

        maxproduct = nums[0]
        minproduct = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            tempmin = min(minproduct * num, num, maxproduct * num)
            maxproduct = max(maxproduct * num, num, minproduct * num)
            minproduct = tempmin
            result = max(result, maxproduct)

        return result

