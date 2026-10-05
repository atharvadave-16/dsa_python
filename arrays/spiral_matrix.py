class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        sr = 0
        sc = 0
        er = len(matrix) -1
        ec = len(matrix[0])-1
        a = []
        while((sr < er +1) and (sc < ec+1)):
            for i in range(sr,ec+1):
                a.append(matrix[sr][i])
            for i in range(sr+1,er+1):
                a.append(matrix[i][ec])     
            if( sr != er):
             for i in range(ec-1, sc-1, -1):
                a.append(matrix[er][i])
            if(sc!=ec):
                for i in range(er-1, sr, -1):
                    a.append(matrix[i][sc])
            sr = sr+1
            sc =sc+1
            er = er-1
            ec=ec-1
        
        return a