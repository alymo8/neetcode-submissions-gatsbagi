class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        seen = {}

        for r in range(len(s)):
            if s[r] in seen and seen[s[r]] >= l:
                l = seen[s[r]] + 1
            
            seen[s[r]] = r
            longest = max(longest, r - l + 1)

        return longest
                
