import heapq
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
       a = [-i for i in stones]
       heapq.heapify(a)
       while len(a) > 1:
        x = -heapq.heappop(a)
        y = -heapq.heappop(a)
        if   x != y :
            heapq.heappush(a, -(x-y))

       return -a[0] if a else 0        