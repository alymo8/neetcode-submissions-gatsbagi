class Solution:
    def rob(self, nums: List[int]) -> int:
        # Start from the end
        # for each index: compare cur + (cur + 2) vs value of cur + 1. 
        # Then choose to rob or not rob

        next1, next2 = 0, 0

        for num in nums:
            temp = max(next1 + num, next2)
            next1 = next2
            next2 = temp
        return next2