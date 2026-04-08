class Solution:

    def characterReplacement(self, s: str, k: int) -> int:
        size = len(s)
        longest = 0
        l = 0

        freqs = [0] * 26

        for r in range(size):
            c = s[r]
            # 
            freqs[ord(c) - ord('A')] += 1
            if r - l + 1 - max(freqs) > k:
                freqs[ord(s[l]) - ord('A')] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest
                



        