def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for ele in nums:
            if nums.count(ele) == 1:
                return ele 

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        a = {}
        for i in nums:
            a[i] = a.get(i,0) + 1
        for key,value in a.items():
            if value == 1:
                return key

def singleNumber(self, nums):
    result = 0
    for n in nums:
        result ^= n  # XOR each number
    return result



# Pattern: Bit Manipulation (XOR)
# Approach: XOR all numbers together, duplicates cancel out
# Key trick: a^a=0, a^0=a → only single number remains
# Brute force: HashMap O(n) space
# Optimal: XOR O(1) space
# TC: O(n) | SC: O(1)