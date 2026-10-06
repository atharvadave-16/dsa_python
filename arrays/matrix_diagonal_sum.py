class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        sum = 0
        a = len(mat)
        b = a -1
        for i in range(0,a):
            sum = sum + mat[i][i]
            if(i != b):
                sum = sum + mat[i][b]
            b = b-1    
        return sum 