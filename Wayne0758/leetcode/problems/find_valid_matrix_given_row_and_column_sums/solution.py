class Solution(object):
    def restoreMatrix(self, rowSum, colSum):
        """
        :type rowSum: List[int]
        :type colSum: List[int]
        :rtype: List[List[int]]
        """
        m=len(rowSum)
        n=len(colSum)
        a=[[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                a[i][j]=min(rowSum[i],colSum[j])
                rowSum[i]-=a[i][j]
                colSum[j]-=a[i][j]
        return a