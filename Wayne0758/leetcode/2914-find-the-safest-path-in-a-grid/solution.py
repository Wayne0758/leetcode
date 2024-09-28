class Solution:
    d = [0,1,0,-1,0]
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        thieves = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    thieves.append((i,j))
                    grid[i][j] = 0
                else:
                    grid[i][j] = -1
        while thieves:
            size = len(thieves)
            while size >0:
                cur = thieves.pop(0)
                for k in range(4):
                    di, dj = cur[0]+self.d[k],cur[1]+self.d[k+1]
                    val = grid[cur[0]][cur[1]]
                    if 0<=di<n and 0<=dj<n and grid[di][dj] == -1:
                        grid[di][dj] = val + 1
                        thieves.append((di, dj))
                size-=1

        start, end, res = 0, 0, -1
        for i in range(n):
            for j in range(n):
                end = max(end, grid[i][j])

        while start <= end:
            mid = start + (end - start) // 2
            if self.isValidSafeness(grid, mid):
                res = mid
                start = mid + 1
            else:
                end = mid - 1

        return res
    def isValidSafeness(self, grid, min_safeness) -> bool:
        n = len(grid)

        if grid[0][0] < min_safeness or grid[n - 1][n - 1] < min_safeness:
            return False

        traversal_queue = deque([(0, 0)])
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True

        while traversal_queue:
            cur = traversal_queue.popleft()
            if cur[0] == n - 1 and cur[1] == n - 1:
                return True 

            for k in range(4):
                di, dj = cur[0]+self.d[k],cur[1]+self.d[k+1]
                if 0<=di<n and 0<=dj<n and not visited[di][dj] and grid[di][dj] >= min_safeness:
                    visited[di][dj] = True
                    traversal_queue.append((di, dj))

        return False
