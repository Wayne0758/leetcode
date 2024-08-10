class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        m = len(grid)
        n = len(grid[0])
        d = [0,1,0,-1,0]
        def dfs(i,j):
            grid[i][j] = '-1'
            flag = 0
            for k in range(4):
                if 0<=i+d[k]<m and 0<=j+d[k+1]<n and grid[i+d[k]][j+d[k+1]] == '1':
                    if not dfs(i+d[k],j+d[k+1]):
                        flag = 1
            if flag == 0:
                return True
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    if dfs(i,j):
                        res+=1
        return res
