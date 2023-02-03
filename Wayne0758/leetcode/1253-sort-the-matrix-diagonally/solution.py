from collections import defaultdict
class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m=len(mat)
        n=len(mat[0])
        a=defaultdict(list)
        for i in range(m):
            for j in range(n):
                heappush(a[i-j],mat[i][j])
        for i in range(m):
            for j in range(n):
                mat[i][j]=heappop(a[i-j])
        return mat
