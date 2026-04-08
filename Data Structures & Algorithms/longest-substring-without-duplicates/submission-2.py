class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        size = len(s)
        l = 0
        longest = 0

        seen = {}
        for r in range(0,size):
            c = s[r]
            if c in seen and seen[c] >= l:
                l = seen[c] + 1

            longest = max(longest, r - l + 1)
            seen[c] = r
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