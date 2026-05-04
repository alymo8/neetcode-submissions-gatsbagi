class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        # cur_length = 0
        seen = {}

        for r in range(len(s)):
            if s[r] in seen and seen[s[r]] >= l:
                l = seen[s[r]] + 1
            seen[s[r]] = r
            longest = max(longest, r - l + 1)
        return longest
            























        # longest = 0
        # current = 0
        # seen = [-1] * 128
        # left = 0
        # for right in range(len(s)):
        #     c = s[right]
        #     if seen[ord(c)] != -1 and seen[ord(c)] >= left:
        #         left = seen[ord(c)] + 1
        #     seen[ord(c)] = right
        #     current = right - left + 1
        #     longest = max(current, longest)
        # return longest