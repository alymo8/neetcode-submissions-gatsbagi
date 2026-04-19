class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        original_len = len(nums)
        k = 0
        while i < len(nums):
            if nums[i-1] == nums[i]:
                nums.pop(i-1)
                k+=1
                i-=1
            i+=1
        return original_len - k
        