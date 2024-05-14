class Solution:
    def assistant(self, grid: List[List[int]], i: int, j: int) -> int:
        m=len(grid)
        n=len(grid[0])
        if i<0 or m<=i or j<0 or n<=j or grid[i][j]==0:
            return 0
        val=grid[i][j]
        mx=0
        grid[i][j]=0
        mx=max(self.assistant(grid, i+1, j), self.assistant(grid, i-1, j), self.assistant(grid, i, j+1), self.assistant(grid, i, j-1))
        grid[i][j]=val
        return val+mx

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        res=0
        for i in range(m):
            for j in range(n):
                res=max(res, self.assistant(grid, i, j))
        return res
