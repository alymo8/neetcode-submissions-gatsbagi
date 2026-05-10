class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [asteroids[0]]

        for i in range(1, len(asteroids)):
            cur = asteroids[i]
            # no collision
            if not stack or stack[-1] < 0 or cur > 0:
                stack.append(cur)
                continue
            
            while stack and stack[-1] * cur < 0:
                destroyed = False
                if abs(cur) > abs(stack[-1]):
                    stack.pop()
                elif abs(cur) == abs(stack[-1]):
                    stack.pop()
                    destroyed = True
                    break
                else:
                    destroyed = True
                    break
            
            if not destroyed:
                stack.append(cur)
        return stack
