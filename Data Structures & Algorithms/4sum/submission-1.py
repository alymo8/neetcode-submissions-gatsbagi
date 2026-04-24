class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = set()

        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                first = nums[i]
                second = nums[j]
                l = j + 1
                r = len(nums) -1
                while l < r:
                    if nums[i] + nums[j] + nums[l] + nums[r] == target:
                        indices = [i, j, l, r]
                        indices.sort()
                        res.add(tuple([nums[index] for index in indices]))
                        l+=1
                    elif nums[i] + nums[j] + nums[l] + nums[r] < target:
                        l+=1
                    else:
                        r-=1
        return list(res)