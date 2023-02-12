class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m=len(grid)
        n=len(grid[0])
        a=[[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                x=i
                y=j+k
                while y>=n:
                    y-=n
                    x+=1
                while x>=m:
                    x-=m
                a[x][y]=grid[i][j]
        return a