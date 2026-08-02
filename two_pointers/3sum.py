class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        res = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
        
        return res



# Pattern: Two Pointers
# Approach: sort, fix i, two pointers l and r for remaining two
# Key trick 1: skip duplicates for i → if i>0 and nums[i]==nums[i-1]
# Key trick 2: skip duplicates for l after finding triplet
# TC: O(n²) | SC: O(1) not counting output    
            