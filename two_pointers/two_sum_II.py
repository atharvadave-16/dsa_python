class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
       a = 0
       b = len(numbers) - 1
       c = numbers[a] + numbers[b]
       while c != target:
        if c > target:
            b = b-1
        if c < target:
            a = a + 1
       return [a+1,b+1]

# two avoid cases with no solution we can use while a<b: