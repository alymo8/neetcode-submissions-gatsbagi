class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        lis = [1] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            max_len = 0
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    max_len = max(lis[j], max_len)
            lis[i] = 1 + max_len            
            
        return max(lis)
                    

           
