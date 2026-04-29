class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        goal = n-1

        for i in range(n-1, -1, -1):
            if nums[i] + i >= goal:
                goal = i
        return goal == 0
        # farthest = 0
       
        # for i in range(n):
        #     if i > farthest:
        #         return False
        #     farthest = max(nums[i] + i, farthest)
        #     if farthest >= n-1:
        #         return True
        # return farthest >= n-1
    


