class Solution(object):
    def oddCells(self, m, n, indices):
        """
        :type m: int
        :type n: int
        :type indices: List[List[int]]
        :rtype: int
        """
        a = [[0 for i in range(n)]for j in range(m)]
        b = 0
        
        for i in range(len(indices)):
            ri,ci = indices[i][0],indices[i][1]
            
            for j in range(m):
                a[j][ci] += 1
            for j in range(n):
                a[ri][j] += 1
                
        for i in range(m):
            for j in range(n):
                if a[i][j]%2 != 0:
                    b += 1
                    
        return b
