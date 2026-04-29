class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        if n == 1:
            return True
        
        closestnon0index = -1
        for i in range(n-2, -1, -1):
            if nums[i] == 0 and closestnon0index == -1:
                closestnon0index = i+1
            elif nums[i] != 0 and closestnon0index != -1 and nums[i] + i >= closestnon0index:
                closestnon0index = -1
        return closestnon0index == -1

