class Solution:
    def rob(self, nums: List[int]) -> int:
        # Start from the end
        # for each index: compare cur + (cur + 2) vs value of cur + 1. 
        # Then choose to rob or not rob

        n = len(nums) - 1
        if n == 0:
            return nums[0]
        elif n == 1:
            return max(nums[0], nums[1])

        tracker = [0] * (len(nums))
        tracker[n] = nums[n]
        tracker[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            tracker[i] = max(tracker[i+1], nums[i] + tracker[i+2])
        
        return tracker[0]
