class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[-1] = True

        n = len(s)
        for i in range(n-1, -1, -1):
            for word in wordDict:
                if n - i >= len(word) and word == s[i:i+len(word)]:
                    dp[i] = dp[i+len(word)]
                if dp[i]:
                    break
        return dp[0]
