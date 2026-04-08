class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        longest = 1
        unique = set(nums)
        
        for i in range(len(nums)):
            if nums[i] - 1 not in unique:
                # start of seq
                len_seq = 1
                check_num = nums[i] + 1
                while check_num in unique:
                    len_seq += 1
                    check_num += 1
                longest = max(longest, len_seq)

        return longest
            
        return result

        