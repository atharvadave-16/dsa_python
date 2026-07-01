from typing import List


def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == target:
                    return True
        return False

#first approach

#binary approach

def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n -1
        while left <= right:
            mid = left + (right - left) // 2
            if self.get(matrix, mid) == target:
                return True
            elif self.get(matrix, mid) < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

       


def get(self, mat, index):
        m ,n = len(mat), len(mat[0])
        i, j = divmod(index, n)
        return mat[i][j]