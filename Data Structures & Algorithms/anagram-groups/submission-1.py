class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []

        seen = {}

        for i in range(len(strs)):
            freqs = [0] * 26
            s = strs[i]
            for c in s:
                freqs[ord(c) - ord('a')] += 1
            f = tuple(freqs)
            if f in seen:
                seen[f].append(s)
            else: seen[f] = [s]
                
        res = [ v for _, v in seen.items()]

        return res