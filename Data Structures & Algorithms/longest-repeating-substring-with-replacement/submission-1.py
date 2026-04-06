class Solution:
    
    def max_freq(self, freqs):
        max_freq = 0
        for v in freqs.values():
            max_freq = max(v, max_freq)
        return max_freq

    def characterReplacement(self, s: str, k: int) -> int:
        freqs = {}
        left = 0
        right = 0
        result = 0
        for right in range(len(s)):
            c = s[right]
            freqs[c] = freqs.get(c, 0) + 1
            window_size = right - left + 1
            if window_size <= k or window_size - self.max_freq(freqs) <= k:
                result = max(result, right - left + 1)

            else:
                # move left
                freqs[s[left]] = freqs[s[left]] -1
                left+=1
        return result



        