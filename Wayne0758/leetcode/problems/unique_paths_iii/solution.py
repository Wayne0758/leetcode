class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        startx=starty=empty=0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j]>=0:
                    empty+=1
                if grid[i][j]==1:
                    startx,starty=i,j
        return self.dfs(grid, startx, starty, empty)
    def dfs(self, grid, x, y, step):
        if grid[x][y]==2:
            return step==1
        res=0
        cur=grid[x][y]
        grid[x][y]=-2
        for dx,dy in [[0,1],[1,0],[0,-1],[-1,0]]:
            nextx, nexty=x+dx,y+dy
            if 0<=nextx<len(grid) and 0<=nexty<len(grid[0]) and grid[nextx][nexty]>=0:
                res+=self.dfs(grid, nextx, nexty, step-1)
        grid[x][y]=cur
        return res