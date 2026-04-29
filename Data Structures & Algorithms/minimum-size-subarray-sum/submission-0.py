class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        # iterate on array
        # window start at l, r = 0
        # if sum(window) < target -> right += 1
        # if sum(window) >= target:
        # while sum >= target
        #   result = max(result, l - r + 1)
        #   l+=1
        # return result

        # tests [1,2,3,4,5] target = 9
        # [10, 1, 2, 3, 4] target = 5
        n = len(nums)

        l = 0
        res = float('inf')
        cursum = 0
        for r in range(0, n):
            cursum += nums[r]
            if cursum < target:
                r += 1
            elif cursum >= target:
                while cursum >= target:
                    res = min(res, r - l + 1)
                    cursum -= nums[l]
                    l+=1
        if res == float('inf'):
            return 0
        return res
                    

