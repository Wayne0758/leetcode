class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0
        if m < 3 and n < 3:
            return 0
        for i in range(1,m-1):
            for j in range(1,n-1):
                if self.ismagicsquare(grid,i,j):
                    res += 1
        return res
    def ismagicsquare(self, grid: List[List[int]], i: int, j: int) -> bool:
        a = [grid[i-1][j-1], grid[i-1][j], grid[i-1][j+1], grid[i][j-1], grid[i][j], grid[i][j+1], grid[i+1][j-1], grid[i+1][j], grid[i+1][j+1]]
        seta = set(a)
        setb = set([1,2,3,4,5,6,7,8,9])
        same = seta & setb
        if len(same) != 9:
            return False
        if a[0] + a[1] + a[2] != 15:
            return False
        if a[3] + a[4] + a[5] != 15:
            return False
        if a[6] + a[7] + a[8] != 15:
            return False
        if a[0] + a[3] + a[6] != 15:
            return False
        if a[1] + a[4] + a[7] != 15:
            return False
        if a[2] + a[5] + a[8] != 15:
            return False
        if a[0] + a[4] + a[8] != 15:
            return False
        if a[2] + a[4] + a[6] != 15:
            return False
        return True
