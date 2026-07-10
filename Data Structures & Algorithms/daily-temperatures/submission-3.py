class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = [(0, temperatures[0])]
        res = [0] * (len(temperatures))

        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                stacki, _ = stack.pop()
                res[stacki] = i - stacki
            stack.append((i,t))
        return res