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