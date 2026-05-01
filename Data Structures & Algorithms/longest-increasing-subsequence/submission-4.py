class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [1] * len(nums)
       
        for i in range(len(nums)-2, -1, -1):
            max_len = -1
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    max_len = max(max_len, lis[j])
            if max_len != -1:
                lis[i] += max_len
        return max(lis)


                    

           
