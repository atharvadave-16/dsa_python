class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        a = set(nums)
        best = 0
        for i in a:
            if (i - 1) not in a:
                length = 0
                while (i + length) in a:
                    length += 1
                best = max(best,length)    
        return(best)

# Pattern: HashSet
# Approach: only start counting from sequence start (i-1 not in set)
# Key trick: checking i-1 avoids counting same sequence multiple times
# TC: O(n) | SC: O(n)   