class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        res = 1

        reiterate = False
        start = True
        prev_res = -1
        while start or reiterate:

            start = False
            reiterate = False
            for i in range(len(nums)):
                if nums[i] == res:
                    res+=1
                elif nums[i] == res + 1:
                    if prev_res == res:
                        reiterate = False
                    else:
                        reiterate = True
                    prev_res = res
        return res