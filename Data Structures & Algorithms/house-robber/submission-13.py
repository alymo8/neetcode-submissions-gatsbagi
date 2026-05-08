class Solution:
    def rob(self, nums: List[int]) -> int:
        # Start from the end
        # for each index: compare cur + (cur + 2) vs value of cur + 1. 
        # Then choose to rob or not rob

        next1, next2 = 0, 0

        for i in range(len(nums) - 1, -1, -1):
            val = max(nums[i] + next2, next1)
            next2 = next1
            next1 = val
        return val