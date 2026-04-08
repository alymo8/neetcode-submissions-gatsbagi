class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        seen = {}
        for s in strs:
            arr = [0] * 26
            for c in s:
                arr[ord(c) - ord('a')] += 1
            key = tuple(arr)
            if key in seen:
                seen[key].append(s)
            else:
                seen[key] = [s]


        for _, v in seen.items():
            result.append(v)
        return result
        
        