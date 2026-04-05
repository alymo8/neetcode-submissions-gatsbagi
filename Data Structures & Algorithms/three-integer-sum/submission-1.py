class Solution:

    def seen_3rd_value(self, value, seen, i, j):
        if value in seen:
            indices = seen[value]
            if indices == None or indices == []:
                return False
            return any(x not in {i, j} for x in indices)
        else: return False


    def threeSum(self, nums: List[int]) -> List[List[int]]:

        seen = {}
        result = set()
        for i in range(len(nums)):
            num = nums[i]
            if num not in seen:
                seen[num] = [i]
            else: 
                seen[num].append(i)
        
        for i in range(len(nums) -1):
            for j in range(i+1, len(nums)):
                num_1 = nums[i]
                num_2 = nums[j]
                # if i not in seen[-num_1 - num_2] and j not in seen[-num_1 - num_2] and
                if self.seen_3rd_value(-(num_1 + num_2), seen, i, j):
                    result.add(tuple(sorted([num_1, num_2, -(num_1 + num_2)])))
        return list(result)