class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = s[0]
        n = len(s)
        for i in range(n):
            l, r = i-1, i+1
            cur = s[i]
            while l >= 0 and r < n:
                if s[l] == s[r]:
                    cur = s[l] + cur + s[r]
                    l-=1
                    r+=1
                    if len(cur) > len(result): 
                        result = cur
                else:
                    break
            l, r = i, i+1
            cur = ""
            while l >= 0 and r < n:
                if s[l] == s[r]:
                    cur = s[l] + cur + s[r]
                    l-=1
                    r+=1
                    if len(cur) > len(result): 
                        result = cur
                else:
                    break
        return result
                    

        