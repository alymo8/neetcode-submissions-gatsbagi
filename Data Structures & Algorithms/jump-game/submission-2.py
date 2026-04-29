class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        if n == 1:
            return True
        
        target_index = -1
        for i in range(n-2, -1, -1):
            if nums[i] == 0 and target_index == -1:
                target_index = i+1
            elif nums[i] != 0 and target_index != -1 and nums[i] + i >= target_index:
                target_index = -1
        return target_index == -1

