class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        a=0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if i+j==len(mat)-1:
                    a+=mat[i][j]
                if i==j:
                    a+=mat[i][j]
        if len(mat)%2==1:
            a-=mat[(len(mat)-1)/2][(len(mat)-1)/2]
        return a