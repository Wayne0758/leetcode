class Solution(object):
    def kInversePairs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        D=[[0 for j in range(1002)] for i in range(1002)]
        D[1][0]=1
        for i in range(2,n+1):
            D[i][0]=1
            for j in range(1,k+1):
                if i>j:
                    D[i][j]=D[i-1][j]+D[i][j-1]
                if i<=j:
                    D[i][j]=D[i][j-1]-D[i-1][j-i]+D[i-1][j]
        return D[n][k]%(1000000007)