class Solution:
    def isHappy(self, n: int) -> bool:
        
        c = 0
        d = False
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            c = 0
            a = list(map(int, str(n)))

            for i in range(len(a)):
                b = a[i] ** 2
                c = c + b

            n = c   

        if n == 1:
            d = True

        return d 