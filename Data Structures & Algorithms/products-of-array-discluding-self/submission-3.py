class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftproduct = [0]* len(nums)
        rightproduct = [0]* len(nums)
        rightproduct[len(nums) - 1] = 1
        leftproduct[0] = 1

        for i in range(1, len(nums)):
            leftproduct[i] = leftproduct[i-1] * nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            rightproduct[i] = rightproduct[i+1] * nums[i+1]

        result = []
        for i in range(len(nums)):
            result.append(leftproduct[i] * rightproduct[i])
        return result






















        # size = len(nums)
        # result = [1] * size
        # # need to have, left product, right product
        # # left_product = [0] * size
        # # right_product = [0] * size

        # # left_product[0] = nums[0]
        # # right_product[size -1] = nums[size-1]
        # prefix = 1
        # for i in range(1, size):
        #     result[i] = prefix * nums[i-1]
        #     prefix *= nums[i-1]

        # suffix = 1
        # for i in range(size-2, -1, -1):
        #     result[i] *= suffix * nums[i+1]
        #     suffix *= nums[i+1]
        # return result

        # # for i in range(size):
        # #     cur = 1
        # #     if i != 0:
        # #         cur = cur * left_product[i-1]
        # #     if i != len(nums) -1:
        # #         cur = cur * right_product[i+1]
        # #     result[i] = cur
