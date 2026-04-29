class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + (r-l) // 2
            res = min(nums[mid], res)
            if nums[mid] >= nums[0]:
                l = mid + 1
            else:
                r = mid -1

        return res
            
            

