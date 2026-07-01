def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        while (len(stones) > 1):
            y = max(stones)
            stones.remove(y)
            x = max(stones)
            stones.remove(x)
            if x != y:
                stones.append(y-x)
        if stones :        
         return stones[0]        
        else: return 0 