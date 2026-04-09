class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        size = len(s)
        last_word = ''
        prev_space = False
        for i,c in enumerate(s):
            if c == ' ':
                prev_space = True
                continue
            else:
                if prev_space:
                    last_word = c
                    prev_space = False
                else:    
                    last_word += c
        return len(last_word)

        