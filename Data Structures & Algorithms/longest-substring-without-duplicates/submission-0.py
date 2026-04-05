class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        current = 0
        seen = [-1] * 128
        left = 0
        for right in range(len(s)):
            c = s[right]
            if seen[ord(c)] != -1 and seen[ord(c)] >= left:
                left = seen[ord(c)] + 1
            seen[ord(c)] = right
            current = right - left + 1
            longest = max(current, longest)
        return longest