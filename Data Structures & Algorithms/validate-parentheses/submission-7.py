class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for c in s:
            if c not in pairs:
                stack.append(c)
            else: # c in close_brackets
                if stack == [] or stack.pop(len(stack) - 1) != pairs[c]:
                    return False
        if stack != []:
            return False
        return True
        