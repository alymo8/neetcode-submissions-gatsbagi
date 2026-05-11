class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_freqs = {}
        for c in t:
            t_freqs[c] = t_freqs.setdefault(c, 0) + 1

        have = 0
        need = len(t_freqs)

        start, res_start, size = 0, 0, float('inf')
        window = {}
        for i, c in enumerate(s):
            window[c] = window.get(c, 0) + 1

            if c in t_freqs and window[c] == t_freqs[c]:
                have += 1
            while have == need:
                if i - start + 1 < size:
                    size = i - start + 1
                    res_start = start
                window[s[start]] -= 1
                if s[start] in t_freqs and window[s[start]] < t_freqs[s[start]]:
                    have -= 1
                start += 1
        return s[res_start: res_start + size ] if size != float('inf') else ""
