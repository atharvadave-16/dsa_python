def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        a, b = 0, 0
        for c in cost:
         a, b = b, c + min(a, b)

        return min(a, b)
