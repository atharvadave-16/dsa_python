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


def containsDuplicate(self, nums):
        unique = set(nums)
        
        if len(unique) != len(nums):
            return True
        else:
            return False