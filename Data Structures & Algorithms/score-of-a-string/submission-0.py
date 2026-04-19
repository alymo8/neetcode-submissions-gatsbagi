class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for i in range(1,len(s)):
            prev = s[i-1]
            cur = s[i]
            score += abs(ord(cur) - ord(prev))
        return score
