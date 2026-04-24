class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        seen = {}
        for c in s1:
            seen[c] = seen.get(c, 0) + 1
        compare = {}
        window = len(s1)

        for i in range(0, window):
            c = s2[i]
            compare[c] = compare.get(c, 0) + 1
        
        if compare == seen:
            return True

        l = 0
        r = window - 1
        while r+1 < len(s2):
            left_char = s2[l]
            compare[left_char] -=1
            if compare[left_char] == 0:
                del compare[left_char]
            
            right_char = s2[r+1]
            compare[right_char] = compare.get(right_char, 0) + 1
            if compare == seen:
                return True
            else:
                l+=1
                r+=1
            
            
        return False
                    
                   
            
            



        