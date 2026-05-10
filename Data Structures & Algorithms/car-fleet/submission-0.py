class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        pairs = [[p, s] for p, s in zip(position, speed)]
        pairs.sort(key = lambda x: x[0], reverse = True)

        for p, s in pairs:
            time_to_dest = (target - p) / s
            if stack and time_to_dest <= stack[-1]:
                continue
            else:
                stack.append(time_to_dest)
           
        return len(stack)
