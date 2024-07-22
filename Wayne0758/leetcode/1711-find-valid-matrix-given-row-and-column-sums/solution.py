class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m = len(rowSum)
        n = len(colSum)
        res = [[0]*n for _ in range(m)]
        while True:
            if sum(rowSum) == 0:
                return res
            minrownum, minrowindex = math.inf, -1
            mincolnum, mincolindex = math.inf, -1
            for i in range(m):
                if rowSum[i] < minrownum and rowSum[i]!=0:
                    minrownum = rowSum[i]
                    minrowindex = i
            for j in range(n):
                if colSum[j] < mincolnum and colSum[j]!=0:
                    mincolnum = colSum[j]
                    mincolindex = j
            if minrownum <= mincolnum:
                res[minrowindex][mincolindex] = minrownum
                rowSum[minrowindex] -= minrownum
                colSum[mincolindex] -= minrownum
            else:
                res[minrowindex][mincolindex] = mincolnum
                rowSum[minrowindex] -= mincolnum
                colSum[mincolindex] -= mincolnum
