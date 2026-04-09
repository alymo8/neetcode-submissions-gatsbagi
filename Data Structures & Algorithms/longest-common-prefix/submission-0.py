class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""

        ref = strs[0]

        for i, c in enumerate(ref):
            is_same = True
            for s in strs:
                if i >= len(s) or s[i] != c:
                    is_same = False
            if is_same:
                result += c
            else:
                return result
        return result
            