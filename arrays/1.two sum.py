nums = list(input())
target = int(input)
for i in range (0,len(nums)-1): 
    for j in range (i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print([i,j])


# Pattern: HashMap
# Approach: for each num check if complement exists in map
# Key trick: store AFTER checking to avoid same index twice
# TC: O(n) | SC: O(n)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
     
     a ={}
     for i in range(len(nums)):
        num = nums[i]
        b = target - num
        if b in a:
          return [a[b], i]
        a[num] = i