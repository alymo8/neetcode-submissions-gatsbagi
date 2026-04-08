class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        cursum = 0

        count = {}
        count[0] = 1
        for i in range(0, len(nums)):
            cursum += nums[i]
            result += count.get(cursum - k, 0)

            count[cursum] = count.get(cursum, 0) + 1
        return result
        
            

            