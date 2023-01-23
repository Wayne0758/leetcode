class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        a=0
        for j in range(len(grid[0])):
            b=0
            for i in range(len(grid)):
                if grid[i][j]>b:
                    b=grid[i][j]
            a+=b
        for i in range(len(grid)):
            while 0 in grid[i]:
                grid[i].remove(0)
            a+=len(grid[i])
            a+=max(grid[i])
        return a