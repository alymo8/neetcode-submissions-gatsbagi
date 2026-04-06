class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_brackets = ['(', '{', '[']
        close_brackets = [')', '}', ']']
        for c in s:
            if c in open_brackets:
                stack.append(c)
            else: # c in close_brackets
                if stack == [] or stack.pop(len(stack) - 1) != open_brackets[close_brackets.index(c)]:
                    return False
        if stack != []:
            return False
        return True
        