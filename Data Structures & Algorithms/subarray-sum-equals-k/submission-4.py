class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        cursum = 0

        count = {0: 1}
        for num in nums:
            cursum += num
            result += count.get(cursum - k, 0)
            count[cursum] = count.get(cursum , 0) + 1
        return result
        
            

            