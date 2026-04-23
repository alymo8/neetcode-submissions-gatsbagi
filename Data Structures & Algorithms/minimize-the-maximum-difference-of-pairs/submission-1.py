class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()

        def can_make_pairs(max_diff: int) -> int:
            count = 0
            i = 0

            while i < len(nums) - 1:
                if abs(nums[i+1] - nums[i]) <= max_diff:
                    count+=1
                    i+=2
                else:
                    i+=1
                if count >= p:
                    return True
            return count >= p

        l = 0
        r = nums[-1] - nums[0]

        while l < r:
            mid = (l+r) // 2
            if can_make_pairs(mid):
                r = mid
            else:
                l = mid+1
        return l
