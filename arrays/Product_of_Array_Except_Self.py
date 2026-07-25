def productExceptSelf(self, nums: list[int]) -> list[int]:
        answer = [1] * len(nums)


        prefix = 1
        for i in range(len(nums)):
         answer[i] = prefix
         prefix *= nums[i]


        suffix = 1
        for i in range(len(nums)-1, -1, -1):
         answer[i] *= suffix
         suffix *= nums[i]

        return answer


# Pattern: Prefix + Suffix product
# Approach: two passes — prefix products left to right, suffix right to left
# Key trick: build directly in answer array, no extra space needed
# prefix pass: answer[i] = product of everything to the left
# suffix pass: answer[i] *= product of everything to the right
# TC: O(n) | SC: O(1) not counting output array

import math
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        if 0 in nums:
            result = [0] * len(nums)
            if nums.count(0) == 1:
                zero_idx = nums.index(0)
                nums.remove(0)
                result[zero_idx] = math.prod(nums)
            return result

        prod = math.prod(nums)
        return [prod // i for i in nums]