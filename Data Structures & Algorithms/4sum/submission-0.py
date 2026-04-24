class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = set()
        # seen = {}

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                first = nums[i]
                second = nums[j]
                if j == i+1:
                    l = i + 2
                else:
                    l = i+1
                if j == len(nums) - 1:
                    r = len(nums) -2
                else:
                    r = len(nums) -1

                while l < r:
                    if nums[i] + nums[j] + nums[l] + nums[r] == target:
                        indices = [i, j, l, r]
                        indices.sort()
                        res.add(tuple([nums[index] for index in indices]))
                        if l+1 != j:
                            l += 1
                        else:
                            l+=2
                    elif nums[i] + nums[j] + nums[l] + nums[r] < target:
                        if l+1 != j:
                            l += 1
                        else:
                            l+=2
                    else:
                        if r-1!= j:
                            r-=1
                        else:
                            r-=2
        return list(res)