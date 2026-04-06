class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums = sorted(nums)
        last_fixed = nums[0]
        for i in range(len(nums)-2):
            fixed = nums[i]
            if fixed == last_fixed and i != 0:
                continue
            last_fixed = fixed
            # target: fixed + nums[left] + nums[right] = 0
            left = i+1
            right = len(nums) - 1
            while left < right:
                if fixed + nums[left] + nums[right] == 0:
                    results.append([fixed, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1

                elif fixed + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1   
        return results
        