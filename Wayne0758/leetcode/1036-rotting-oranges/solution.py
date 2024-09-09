class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        fresh = 0
        d = [0,1,0,-1,0]
        queue = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                    flag=0
                    for k in range(4):
                        if 0<=i+d[k]<m and 0<=j+d[k+1]<n and grid[i+d[k]][j+d[k+1]]!=0:
                            flag=1
                    if flag == 0:
                        return -1
                elif grid[i][j] == 2:
                    queue.append([i,j])
        second_queue = []
        res = 0
        while queue:
            while queue:
                [i,j] = queue.pop(0)
                for k in range(4):
                    if 0<=i+d[k]<m and 0<=j+d[k+1]<n and grid[i+d[k]][j+d[k+1]]==1:
                        grid[i+d[k]][j+d[k+1]]=2
                        fresh -= 1
                        second_queue.append([i+d[k], j+d[k+1]])
            queue = second_queue
            second_queue = []
            res+=1
        if fresh!=0:
            return -1
        return max(0,res-1)
