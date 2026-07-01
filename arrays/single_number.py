def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for ele in nums:
            if nums.count(ele) == 1:
                return ele 