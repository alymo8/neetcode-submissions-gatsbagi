class Solution:
    def firstUniqChar(self, s: str) -> str:

        seen = {}
        for c in s:
            seen[c] = seen.get(c, 0) + 1
        char = ''
        for c in seen:
            if seen[c] == 1:
                char = c
                break

        for i,c in enumerate(s):
            if c == char:
                return i

        if char == '':
            return -1

                