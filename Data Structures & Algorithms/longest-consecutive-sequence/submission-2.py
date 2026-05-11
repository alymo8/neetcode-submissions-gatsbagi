class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # create set from numbers
        # vars longest, seq_len

        # iterate on nums, if nums[i] - 1 not in set
        #   then it's a new seq, keep checking for nums[i] + 1 
        #   and update seq_len
        
        unique = set(nums)

        longest = 0
        for i, num in enumerate(nums):
            cur_seq = 0
            if num - 1 not in unique:
                # start of a seq
                val = num
                while val in unique:
                    cur_seq += 1
                    longest = max(longest, cur_seq)
                    val += 1
        return longest
                


