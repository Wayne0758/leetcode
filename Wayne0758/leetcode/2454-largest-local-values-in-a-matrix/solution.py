class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        n=len(grid)
        c=[]
        for i in range(n-2):
            b=[]
            for j in range(n-2):
                a=0
                for k in range(3):
                    for l in range(3):
                        if grid[i+k][j+l]>a:
                            a=grid[i+k][j+l]
                b.append(a)
            c.append(b)
        return c
