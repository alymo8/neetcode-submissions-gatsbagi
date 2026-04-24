class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = set()

        for i in range(len(nums)):
            l = i+1
            r = len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    key = tuple([nums[i], nums[l], nums[r]])
                    res.add(key)
                    l+=1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l+=1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r-=1
        return list(res)
    
