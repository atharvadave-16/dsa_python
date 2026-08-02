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


# Pattern: Min Heap of size k
# Approach: maintain min heap of exactly k largest elements
# Key trick: heap[0] always = kth largest (smallest of k largest)
# self.variables to share data between __init__ and add()
# TC: O(log k) per add | SC: O(k)        