class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        l = 0
        r = n - 1

        look_left = False
        if target >= nums[0]:
            look_left = True

        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[0] and look_left:
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid-1
            elif nums[mid] >= nums[0] and not look_left:
                l = mid+1
            elif nums[mid] < nums[0] and look_left:
                r = mid -1
            elif nums[mid] < nums[0] and not look_left:
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid-1
        return -1