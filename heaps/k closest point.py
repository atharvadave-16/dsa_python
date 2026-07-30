import heapq
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
     heap = []
     for x, y in points:
        dist = x**2 + y**2
        heapq.heappush(heap, (dist, x, y))  # push tuple
    
     result = []
     for _ in range(k):
        _, x, y = heapq.heappop(heap)  # pop k smallest
        result.append([x, y])
     return result


# Pattern: Min Heap
# Approach: push (dist, x, y) tuples, pop k times for k closest
# Key trick: x**2 + y**2 (no sqrt needed, just comparing distances)
# Tuple in heap → sorts by first element (dist) automatically
# _ or d for ignored values when unpacking tuples
# TC: O(n log n) | SC: O(n)    