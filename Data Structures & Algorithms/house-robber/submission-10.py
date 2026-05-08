class Solution:
    def rob(self, nums: List[int]) -> int:
        # Start from the end
        # for each index: compare cur + (cur + 2) vs value of cur + 1. 
        # Then choose to rob or not rob

        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums)

        r = nums[n-1]
        l = nums[n-2]
        val = max(r, l)

        for i in range(n-3, -1, -1):
            val = max(nums[i] + r, l)
            r = l
            l = val

        return val
