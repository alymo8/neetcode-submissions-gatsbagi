class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        seen = {}
        for c in s1:
            seen[c] = seen.get(c, 0) + 1

        l = 0
        r = len(s1) - 1
        while r < len(s2):
            compare = {}
            for i in range(l, r+1):
                c = s2[i]
                if c in seen:
                    compare[c] = compare.get(c,0) + 1
                if c not in seen or compare[c] > seen[c]:
                    break
            if seen == compare:
                return True
            l+=1
            r+=1
        return False
                    
                   
            
            



        