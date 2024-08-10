class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        reintepret = [[0] * (3*n) for _ in range(3*n)]
        res = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == '/':
                    reintepret[3*i+2][3*j] = 1
                    reintepret[3*i+1][3*j+1] = 1
                    reintepret[3*i][3*j+2] = 1
                elif grid[i][j] == '\\':
                    reintepret[3*i][3*j] = 1
                    reintepret[3*i+1][3*j+1] = 1
                    reintepret[3*i+2][3*j+2] = 1
        d = [0,1,0,-1,0]
        def findspace(i,j):
            reintepret[i][j]=-1
            flag = 0
            for k in range(4):
                if 0<=i+d[k]<3*n and 0<=j+d[k+1]<3*n:
                    if reintepret[i+d[k]][j+d[k+1]]==0:
                        if not findspace(i+d[k],j+d[k+1]):
                            flag = 1
            if flag == 0:
                return True
        for i in range(3*n):
            for j in range(3*n):
                if reintepret[i][j]==0:
                    if findspace(i,j):
                        res+=1
        return res
