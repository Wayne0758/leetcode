class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        a=[]
        for j in range(len(matrix[0])):
            x=0
            for i in range(len(matrix)):
                if matrix[i][j]>x:
                    x=matrix[i][j]
            a.append(x)
        b=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==min(matrix[i]) and matrix[i][j]==a[j]:
                    b.append(matrix[i][j])
        return b
