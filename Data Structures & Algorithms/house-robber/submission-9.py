class Solution:
    def rob(self, nums: List[int]) -> int:
        # Start from the end
        # for each index: compare cur + (cur + 2) vs value of cur + 1. 
        # Then choose to rob or not rob

        n = len(nums) - 1
        if n == 0:
            return nums[0]
        res = 0

        tracker = [0] * (len(nums))
        r = nums[n]
        l = max(nums[n], nums[n-1])
        for i in range(n-2, -1, -1):
            res = max(l, nums[i] + r)
            r = l
            l = res

        
        return l
