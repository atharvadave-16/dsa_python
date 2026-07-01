def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        a = []

        for i in nums:
         count[i] = 1 + count.get(i, 0)

        while k != 0:
         b = max(count.values())

         for key in list(count.keys()):
            if count[key] == b:
              a.append(key)
              del count[key]
              k -= 1
              break

        return a
