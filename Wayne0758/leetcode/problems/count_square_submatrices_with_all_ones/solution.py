class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0
        s=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i!=0 and j!=0 and matrix[i][j]==1:
                    matrix[i][j]=min([matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1]])+matrix[i][j]
                s+=matrix[i][j]
        return s