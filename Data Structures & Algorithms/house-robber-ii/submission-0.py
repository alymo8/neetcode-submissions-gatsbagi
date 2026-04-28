class Solution:
   
    def rob_helper(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        l = max(nums[n-1], nums[n-2])
        r = nums[n-1]
        res = 0
        for i in range(n-3, -1, -1):
            res = max(nums[i] + r, l)
            r = l
            l = res
        return l



    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])

        copy1 = nums[:-1]
        copy2 = nums[1:]
        return max(self.rob_helper(copy1), self.rob_helper(copy2))

