class Solution:
    def __init__(self):
        self.grid = [[]]
        self.direct = [0,1,0,-1,0]
        self.m = 0
        self.n = 0
        self.bfs_queue = []
        self.res = 0
    def shortestBridge(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])
        for i in range(self.m):
            flag=0
            for j in range(self.n):
                if grid[i][j] == 1:
                    self.dfs(i, j)
                    flag=1
                    break
            if flag==1:
                break
        res = 0
        self.bfs()
        return self.res-1
    def bfs(self):
        self.res += 1
        new_bfs = []
        while self.bfs_queue:
            [i, j] = self.bfs_queue.pop(-1)
            for k in range(1, len(self.direct)):
                nxi, nxj = i+self.direct[k], j+self.direct[k-1]
                if 0 <= nxi < self.m and 0 <= nxj < self.n:
                    if self.grid[nxi][nxj] == 0:
                        self.grid[nxi][nxj] = -1
                        new_bfs.append([nxi, nxj])
                    if self.grid[nxi][nxj] == 1:
                        return
        self.bfs_queue = new_bfs
        self.bfs()
    def dfs(self, i, j):
        self.grid[i][j] = 2
        self.bfs_queue.append([i, j])
        for k in range(1, len(self.direct)):
            nxi, nxj = i+self.direct[k], j+self.direct[k-1]
            if 0 <= nxi < self.m and 0 <= nxj < self.n:
                if self.grid[nxi][nxj] == 1:
                    self.dfs(nxi, nxj)
