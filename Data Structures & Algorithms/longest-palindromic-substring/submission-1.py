class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0]

        n = len(s)

        for i in range(n):
            # case odd size
            l = i - 1
            r = i + 1
            cur = s[i]
            while l >= 0 and r < n:
                if s[l] == s[r]:
                    cur = s[l] + cur + s[r]
                    l-=1
                    r+=1
                    if len(cur) > len(res):
                        res = cur
                else:
                    break 
            
            l = i
            r = i + 1
            cur = ""
            while l >= 0 and r < n:
                if s[l] == s[r]:
                    cur = s[l] + cur + s[r]
                    l-=1
                    r+=1
                    if len(cur) > len(res):
                        res = cur
                else:
                    break
        return res
                    

        