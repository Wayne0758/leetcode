class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        empty = []
        filled = []
        self.res = float('inf')
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 0:
                    empty.append((i,j))
                if grid[i][j] >= 2:
                    for _ in range(grid[i][j]-1):
                        filled.append((i,j))
        def solve(i,a,b,vis,c,s):
            if c == len(b):
                self.res = min(self.res,s)
                return
            for j in range(len(b)):
                if vis[j] == 1:
                    continue
                vis[j]=1
                x = abs(a[i][0]-b[j][0])+abs(a[i][1]-b[j][1])
                solve(i+1,a,b,vis,c+1,s+x)
                vis[j]=0
                

        visited = [0 for _ in range(len(empty))]
        solve(0,filled,empty,visited,0,0)
        return self.res
