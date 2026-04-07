class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        if len(t) != len(s):
            return False
        for c in s:
            seen[c] = seen.get(c, 0) + 1
        for c in t:
            if c not in seen:
                return False
            else:
                seen[c] = seen[c] -1
                if seen[c] == -1:
                    return False
        
        return True
        