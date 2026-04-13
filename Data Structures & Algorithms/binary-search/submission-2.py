class Solution:
       
    def binary(self, nums, target, left, right):
        if left > right:
            return -1
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
            return self.binary(nums, target, left, right)
        else:
            right = mid - 1
            return self.binary(nums, target, left, right)


    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) -1
        return self.binary(nums, target, left, right)


        