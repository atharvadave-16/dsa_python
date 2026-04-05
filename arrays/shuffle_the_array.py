def shuffle(self, nums: list[int], n: int) -> list[int]:
        a = len(nums)//2
        b = nums[:a]
        c= nums[a:]
        d =[]
        for i in range(0,len(b)):
         d.append(b[i])