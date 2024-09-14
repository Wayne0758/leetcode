class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        d = [0,1,0,-1,0]
        traveled = [[0]*n for _ in range(m)]
        traveled[0][0] = -1
        res = [matrix[0][0]]
        k = 0
        i = 0
        j = 0
        while True:
            if len(res) == m*n:
                return res
            if i+d[k]>=m or i+d[k]<0 or j+d[k+1]>=n or j+d[k+1]<0 or traveled[i+d[k]][j+d[k+1]] == -1:
                k = (k+1)%4
            i += d[k]
            j += d[k+1]
            res.append(matrix[i][j])
            traveled[i][j] = -1
        return res
