import heapq
class KthLargest:

    def __init__(self, k: int, nums: list[int]):
     self.a = k
     self.b = nums
     heapq.heapify(nums)
     while len(nums)>k:
        heapq.heappop(nums)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.b,val)
        if len(self.b) > self.a:
            heapq.heappop(self.b)
        return self.b[0]