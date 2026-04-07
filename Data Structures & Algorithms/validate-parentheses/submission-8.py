class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for c in s:
            if c not in brackets:
                stack.append(c)
            else:
                if stack == [] or stack.pop(len(stack) - 1) != brackets[c]:
                    return False
        return stack == []