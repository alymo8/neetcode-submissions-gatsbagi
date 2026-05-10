class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for i in range(len(tokens)):
            t = tokens[i]
            if t == "+":
                local = stack.pop() + stack.pop()
                stack.append(local)                
            elif t == "-":
                local = -stack.pop() + stack.pop()
                stack.append(local)
            elif t == "*":
                local = stack.pop() * stack.pop()
                stack.append(local)
            elif t == "/":
                denom = stack.pop()
                nom = stack.pop()
                stack.append(int(nom / denom))
            else:
                stack.append(int(t))
        return stack[0]

                