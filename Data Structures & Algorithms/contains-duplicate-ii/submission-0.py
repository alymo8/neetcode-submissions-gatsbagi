class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        for i in range (len(nums)):
            cur = nums[i]
            if cur in seen and i - seen[cur] <= k:
                return True
            else:
                seen[cur] = i
        return False
