class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # [30,38,30,36,35,40,28]
        # [ 1  4  0  2  1  0  0]
        if len(temperatures) == 0:
            return 0

        result = [0] * len(temperatures)

        # push temp, index to stack
        # when you see a tempearature, 
        # start poping until it's not warmer than in stack
        # for those popped, insert curi - stacki to index stacki
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][1]:
                stacki, stack_temp = stack.pop()
                result[stacki] = i - stacki
            
            stack.append([i, temperatures[i]])
        return result