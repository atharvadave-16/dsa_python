class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
         a = {}
         for i in nums:
             a[i] = a.get(i, 0) + 1
    
   
         sorted_keys = sorted(a, key=a.get, reverse=True)
         return sorted_keys[:k]
    
# Pattern: HashMap + Sorting
# Approach: count frequencies in hashmap, sort by frequency, return top k
# Key trick: a.get(i, 0) + 1 to build frequency map cleanly
# sorted syntax: sorted(a, key=a.get, reverse=True) → sort keys by their values, highest first
# Optimal: heap gives O(n log k) but requires heap knowledge
# TC: O(n log n) | SC: O(n)