class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        nums = people
        
        nums.sort()

        l= 0
        r = len(nums) - 1

        total = 0


        while l < r:
            if nums[l] + nums[r] > limit:
                total += 1
                r -= 1
            elif nums[l] + nums[r] <= limit:
                total += 1
                l+=1
                r -= 1
        if l == r:
            total+=1
        return total
                    
                
                