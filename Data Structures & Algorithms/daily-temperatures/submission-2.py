class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = [(0, temperatures[0])]
        result = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                stacki, stackt = stack.pop()
                result[stacki] = i - stacki
            stack.append((i, t))
        return result
            