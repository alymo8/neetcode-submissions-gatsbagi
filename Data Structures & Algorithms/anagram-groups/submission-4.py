class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for s in strs:
            key = "".join(sorted(s))
            val = seen.get(key, [])
            val.append(s)
            seen[key] = val

        return list(seen.values())
