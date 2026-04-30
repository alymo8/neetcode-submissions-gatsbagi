class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = {}

        for word in strs:
            arr = [0] * 26
            for c in word:
                arr[ord(c) - ord('a')]+= 1
            key = tuple(arr)
            value = res.get(key, [])
            value.append(word)
            res[key] = value
        return list(v for _,v in res.items())

