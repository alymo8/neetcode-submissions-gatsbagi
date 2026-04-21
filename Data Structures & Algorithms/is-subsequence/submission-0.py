class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        curs = 0
        for i in range(len(t)):
            if curs < len(s) and t[i] == s[curs]:
                curs+=1
        if curs == len(s):
            return True
        return False