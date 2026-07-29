import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums = [-i for i in nums]
        heapq.heapify(nums)
        for j in range(0,k):
            a = -heapq.heappop(nums)
        return a



import heapq
class Solution:
    def findKthLargest(self, nums, k):
        heap = nums[:k]        # first k elements
        heapq.heapify(heap)    # min heap of size k
        
        for n in nums[k:]:     # remaining elements
            if n > heap[0]:    # bigger than smallest in heap
                heapq.heappop(heap)
                heapq.heappush(heap, n)
        
        return heap[0]         # smallest of k largest = kth largest    

# Pattern: Heap
# Approach 1: max heap → pop k times → last pop is kth largest
# Approach 2: min heap size k → top is always kth largest
# Key trick: negate for max heap in Python
# TC: O(n + k log n) approach 1 | O(n log k) approach 2
# SC: O(n)
   