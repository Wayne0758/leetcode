class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        a=[]
        for i in range(len(mat)):
            a.append([i,mat[i].count(1)])
        a.sort(key = lambda x:x[1])
        b=[]
        for i in range(k):
            b.append(a[i][0])
        return b