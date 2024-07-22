class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        res = []
        m = len(matrix)
        n = len(matrix[0])
        min_in_row = []
        for i in range(m):
            min_in_row.append(min(matrix[i]))
        for j in range(n):
            temp = 0
            for i in range(m):
                if matrix[i][j] > temp:
                    temp = matrix[i][j]
            if temp in min_in_row:
                res.append(temp)
        return res
