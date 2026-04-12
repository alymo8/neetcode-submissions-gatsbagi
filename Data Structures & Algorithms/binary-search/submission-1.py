class Solution:

    def searchhelp(self, nums, target, left, right, curi):
        if left > right:
            return -1
        
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid-1
        elif nums[mid] < target:
            left = mid + 1
        return self.searchhelp(nums, target, left, right, mid)
       


    def search(self, nums: List[int], target: int) -> int:
        curi = len(nums) // 2
        left = 0
        right = len(nums) - 1
        return self.searchhelp(nums, target, left, right, curi)


        