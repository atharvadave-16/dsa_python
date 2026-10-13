class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(0,n-1):
            for j in range(0,n-1-i):
                if nums[j]>nums[j+1]:
                    t = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = t