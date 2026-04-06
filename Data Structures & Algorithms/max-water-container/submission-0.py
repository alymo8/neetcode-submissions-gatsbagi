class Solution:
    
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        total = 0
        while left < right:
            current = (right - left) * min(heights[right], heights[left])
            total = max(current, total)
            if heights[left] <= heights[right]:
                left += 1
            elif heights[right] < heights[left]:
                right -=1
        return total
                