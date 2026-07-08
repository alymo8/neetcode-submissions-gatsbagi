class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        result = -1

        l = 0
        r = len(heights) - 1

        while l < r:
            result = max(result, min(heights[r], heights[l]) * (r - l))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return result
