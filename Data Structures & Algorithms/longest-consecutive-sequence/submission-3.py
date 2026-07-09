class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # is start -> x - 1 not in list
        # keep checking that x + 1 is in set
        # compare len

        nums = set(nums)

        longest = 0
        for num in nums:
            cur_len = 0
            if num - 1 not in nums:
                cur_num = num
                while cur_num in nums:
                    cur_len += 1
                    cur_num += 1
            longest = max(longest, cur_len)
        return longest
