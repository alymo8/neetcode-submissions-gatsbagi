class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''

        # strdigits = (digits)
        for i in range(len(digits)):
            s = s + str(digits[i])
    
        val = int(s) + 1
        valstr = str(val)
        result = []
        for i in range(len(valstr)):
            result.append(int(valstr[i]))

        return result


        