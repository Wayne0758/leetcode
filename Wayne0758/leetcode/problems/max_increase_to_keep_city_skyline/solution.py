class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        a=[]
        b=[]
        s=0
        for j in range(len(grid)):
            m=0
            for i in range(len(grid)):
                if grid[i][j]>m:
                    m=grid[i][j]
            a.append(m)
        for i in range(len(grid)):
            n=max(grid[i])
            b.append(n)
        for i in range(len(grid)):
            for j in range(len(grid)):
                s+=(min(a[j],b[i])-grid[i][j])
        return s