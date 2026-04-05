def shuffle(self, nums: List[int], n: int) -> List[int]:
        a = len(nums)//2
        b = nums[:a]
        c= nums[a:]
        d =[]
        for i in range(0,len(b)):
         d.append(b[i])