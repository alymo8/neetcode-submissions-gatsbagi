class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # seen = {}

        # for num in nums:
        #     seen[num] = seen.get(num, 0) + 1
        setx = set()

        for i in range(len(nums)-1):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] + nums[i] == 0:
                    t = tuple([nums[i], nums[l], nums[r]])
                    setx.add(t)
                    l+=1
                elif nums[l] + nums[r] + nums[i] < 0:
                    l +=1
                else:
                    r -=1
        return list(setx)