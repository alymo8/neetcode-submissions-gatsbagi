class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = [asteroids[0]]

        for i in range(1, len(asteroids)):
            
            if not stack or asteroids[i] > 0 or stack[-1] < 0:
                stack.append(asteroids[i])
                continue
            
            cur = asteroids[i]
            while stack and cur * stack[-1] < 0:
                if abs(cur) > abs(stack[-1]):
                    stack.pop()
                elif abs(cur) == abs(stack[-1]):
                    stack.pop()
                    break
                else: break
            else:
                stack.append(cur)
            
        return stack