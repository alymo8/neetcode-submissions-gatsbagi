class Solution:
    def minWindow(self, s: str, t: str) -> str:

        result = [float('-inf'),float('inf')]
        result_changed = False

        tmap = {}
        for c in t:
            tmap[c] = tmap.get(c, 0) + 1
        need = len(tmap.keys())
        have = 0

        wmap = {}

        l = 0
        for r in range(len(s)):
            c = s[r]
            if c in tmap:
                prev = wmap.get(c,0)
                wmap[c] = wmap.get(c,0) + 1

                if wmap[c] >= tmap[c] and prev < tmap[c]:
                    have += 1

                while have == need and l <= r:
                    if result[1] - result[0] + 1 > r - l + 1:
                        result_changed = True
                        result = [l, r]
                        # return s[result[0]:result[1] + 1] + ' ' +  str(result[0]) + ' ' + str(result[1]) + ' ' +  str(have) + ' ' +  str(need)
                # shrink from left
                    if l < len(s) and s[l] in wmap:
                        # return s[result[0]:result[1] + 1] + ' ssss ' +  str(result[0]) + ' ' + str(result[1]) + ' ' +  str(have) + ' ' +  str(need)
                        wmap[s[l]] -= 1
                        if wmap[s[l]] < tmap[s[l]]:
                            have -=1
                    l+=1
        if result_changed:
            return  s[result[0]:result[1] + 1]
        else: 
            return ""

        