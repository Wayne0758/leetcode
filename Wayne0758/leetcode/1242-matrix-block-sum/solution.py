class Solution(object):
    def matrixBlockSum(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m=len(mat)
        n=len(mat[0])
        matrix=[[0 for i in range(n+1)] for j in range(m+1)]
        res=[[0 for i in range(n)] for j in range(m)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                matrix[i][j]=matrix[i-1][j]+matrix[i][j-1]+mat[i-1][j-1]-matrix[i-1][j-1]
        for i in range(m):
            for j in range(n):
                row0 ,col0=max(i-k,0),max(j-k,0)
                row1 ,col1=min(i+k,m-1),min(j+k,n-1)
                res[i][j]=matrix[row1+1][col1+1]-matrix[row0][col1+1]-matrix[row1+1][col0]+matrix[row0][col0]
        return res
