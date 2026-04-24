class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        count = {}
        for n in nums:
            count[n] = count.get(n,0) + 1
            if len(count) <= 2:
                continue

            update_count = {}
            for n2,c in count.items():
                if c > 1:
                    update_count[n2] = c-1
            count = update_count
        res = []

        for n in count.keys():
            if nums.count(n) > len(nums) // 3:
                res.append(n)
        return res
