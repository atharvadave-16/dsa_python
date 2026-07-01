def twoSum(self, numbers: list[int], target: int) -> list[int]:
        p1 = 0
        p2 = len(numbers) - 1
        while numbers[p1] + numbers[p2] != target:
            if numbers[p1] + numbers[p2] > target:
                p2 = p2-1
            else:p1 = p1+1    
        return [p1+1,p2+1]

# two avoid cases with no solution we can use while p1<p2: