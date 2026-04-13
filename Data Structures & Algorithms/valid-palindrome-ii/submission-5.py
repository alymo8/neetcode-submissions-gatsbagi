class Solution:
    def validPalindrome(self, s: str) -> bool:
        def ispalindrome(sub):
            l = 0
            r = len(sub) -1
            while l < r:
                if sub[l] != sub[r]:
                    return False
                l+=1
                r-=1
            return True

        left = 0
        right = len(s) -1
        while left < right:
            if s[left] != s[right]:
                return ispalindrome(s[left+1:right+1]) or ispalindrome(s[left:right])
            left+=1
            right -=1

        return True

