class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        res = len(nums)
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                res = mid
                r = mid - 1
            else:
                # res = nums[mid]
                l = mid+1
        return res