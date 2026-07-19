class Solution:
    def hammingWeight(self, n: int) -> int:
        a = str(bin(n))
        b =0
        for i in a:
            if i ==  "1":
                b = b +1
        return b  