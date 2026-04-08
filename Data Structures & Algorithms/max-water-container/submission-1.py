class Solution:
    
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) -1
        res = 0
        while left < right:
            if heights[left] < heights[right]:
                res = max((right - left) * heights[left], res)
                left += 1
            else:
                res = max((right - left) * heights[right], res)
                right -= 1
        return res