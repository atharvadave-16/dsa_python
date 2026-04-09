def longestConsecutive(self, nums: list[int]) -> int:
        a = set(nums)
        count = []
        for i in a:
            if (i - 1) not in a:
                length = 0
                while (i + length) in a:
                    length += 1
                count.append(length)    
        return(max(count))  if count else 0 