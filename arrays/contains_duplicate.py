def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        seen = set()
        for ele in nums:
            if ele in seen:
                return True
            seen.add(ele)
        return False


# Pattern: Set
# Approach: set removes duplicates, compare lengths
# Key trick: len(set(nums)) != len(nums) means duplicate exists
# TC: O(n) | SC: O(n)

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        a = set(nums)
        if len(a) != len(nums):
            return True
        else : return False