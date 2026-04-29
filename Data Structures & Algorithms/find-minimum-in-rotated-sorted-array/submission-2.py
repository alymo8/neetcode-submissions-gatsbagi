class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        n = len(nums)

        l = 0
        r = n - 1

        while l <= r:
            mid = l + (r - l) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[0]:
                l = mid + 1
            elif nums[mid] < nums[0]:
                r = mid - 1
        return res 