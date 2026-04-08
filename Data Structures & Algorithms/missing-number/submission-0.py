class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = -1
        seen = [False] * (len(nums) +1)
        for num in nums:
            seen[num] = True
        for i in range(len(seen)):
            num = seen[i]
            if num == False:
                return i
